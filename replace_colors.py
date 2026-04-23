"""
replace_colors.py
-----------------
Replaces specific colors in all PNG files inside a folder.
Uses only Python standard library — no third-party packages needed.

HOW TO USE:
1. Edit COLOR_PAIRS below — each entry is (old_color, new_color) as RGB or RGBA tuples.
2. Set INPUT_FOLDER and OUTPUT_FOLDER (can be the same folder to overwrite in place).
3. Run:  python replace_colors.py
"""

import struct
import zlib
from pathlib import Path

# ─────────────────────────────────────────────
#  CONFIGURATION — edit these
# ─────────────────────────────────────────────

INPUT_FOLDER  = "./sunny"
OUTPUT_FOLDER = "./sunny"

# Color pairs: (OLD color → NEW color)
# Use 3-tuples (R,G,B) for RGB PNGs, or 4-tuples (R,G,B,A) for RGBA PNGs.
COLOR_PAIRS = [
    ((221, 221, 221), ( 39,   45,  97)),
    ((161, 161, 161), (255,  122,  53)),
    ((121, 121, 121), (255,  182,  105)),
    (( 71,  71,  71), (255,  227,  118)),
    ((  0,   0,   0), (255,  227,  118)),
]

# Tolerance: 0 = exact match only, higher values also catch near-matching pixels
TOLERANCE = 0

# ─────────────────────────────────────────────
#  PNG READER / WRITER  (stdlib only)
# ─────────────────────────────────────────────

PNG_SIGNATURE = b'\x89PNG\r\n\x1a\n'


def read_chunks(data: bytes):
    pos = 8
    while pos < len(data):
        length = struct.unpack('>I', data[pos:pos+4])[0]
        chunk_type = data[pos+4:pos+8]
        chunk_data = data[pos+8:pos+8+length]
        pos += 12 + length
        yield chunk_type, chunk_data


def write_chunk(chunk_type: bytes, data: bytes) -> bytes:
    crc = zlib.crc32(chunk_type + data) & 0xFFFFFFFF
    return struct.pack('>I', len(data)) + chunk_type + data + struct.pack('>I', crc)


def paeth_predictor(a, b, c):
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    elif pb <= pc:
        return b
    return c


def unfilter_row(filter_type, row, prev_row, channels):
    row = bytearray(row)
    n = len(row)
    if filter_type == 0:
        pass
    elif filter_type == 1:
        for i in range(channels, n):
            row[i] = (row[i] + row[i - channels]) & 0xFF
    elif filter_type == 2:
        for i in range(n):
            row[i] = (row[i] + prev_row[i]) & 0xFF
    elif filter_type == 3:
        for i in range(n):
            a = row[i - channels] if i >= channels else 0
            row[i] = (row[i] + (a + prev_row[i]) // 2) & 0xFF
    elif filter_type == 4:
        for i in range(n):
            a = row[i - channels] if i >= channels else 0
            b = prev_row[i]
            c = prev_row[i - channels] if i >= channels else 0
            row[i] = (row[i] + paeth_predictor(a, b, c)) & 0xFF
    return bytes(row)


def decode_png(raw: bytes):
    assert raw[:8] == PNG_SIGNATURE, "Not a valid PNG file"

    ihdr_data = None
    idat_parts = []
    extra_chunks = []

    for chunk_type, chunk_data in read_chunks(raw):
        if chunk_type == b'IHDR':
            ihdr_data = chunk_data
        elif chunk_type == b'IDAT':
            idat_parts.append(chunk_data)
        elif chunk_type != b'IEND':
            extra_chunks.append((chunk_type, chunk_data))

    # Parse IHDR manually to avoid struct format length mistakes
    width      = struct.unpack('>I', ihdr_data[0:4])[0]
    height     = struct.unpack('>I', ihdr_data[4:8])[0]
    bit_depth  = ihdr_data[8]
    color_type = ihdr_data[9]

    assert bit_depth == 8, f"Only 8-bit PNGs supported (got {bit_depth}-bit)"
    assert color_type in (2, 6), (
        f"Only RGB (type 2) and RGBA (type 6) PNGs supported (got type {color_type}). "
        "Indexed/palette PNGs are not supported."
    )

    channels = 3 if color_type == 2 else 4
    raw_image = zlib.decompress(b''.join(idat_parts))
    stride = width * channels

    pixels = []
    pos = 0
    prev_row = bytes(stride)
    for _ in range(height):
        filter_type = raw_image[pos]
        pos += 1
        row = raw_image[pos:pos + stride]
        pos += stride
        row = unfilter_row(filter_type, row, prev_row, channels)
        pixels.append(bytearray(row))
        prev_row = row

    return width, height, pixels, color_type, extra_chunks


def encode_png(width, height, pixels, color_type, extra_chunks) -> bytes:
    # IHDR must be exactly 13 bytes: width(4) + height(4) + 5 single bytes
    ihdr = struct.pack('>II5B', width, height, 8, color_type, 0, 0, 0)

    raw_rows = bytearray()
    for row in pixels:
        raw_rows.append(0)  # filter type: None
        raw_rows.extend(row)

    out = PNG_SIGNATURE
    out += write_chunk(b'IHDR', ihdr)
    for ct, cd in extra_chunks:
        out += write_chunk(ct, cd)
    out += write_chunk(b'IDAT', zlib.compress(bytes(raw_rows), 9))
    out += write_chunk(b'IEND', b'')
    return out


# ─────────────────────────────────────────────
#  COLOR REPLACEMENT
# ─────────────────────────────────────────────

def replace_colors(pixels, channels, pairs, tol):
    counts = [0] * len(pairs)
    for row in pixels:
        for px in range(0, len(row), channels):
            for idx, (old_color, new_color) in enumerate(pairs):
                if all(abs(int(row[px + i]) - int(old_color[i])) <= tol
                       for i in range(len(old_color))):
                    for c, val in enumerate(new_color):
                        row[px + c] = val
                    counts[idx] += 1
                    break
    return counts


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

def main():
    input_path  = Path(INPUT_FOLDER)
    output_path = Path(OUTPUT_FOLDER)
    output_path.mkdir(parents=True, exist_ok=True)

    png_files = list(input_path.glob("*.png"))
    if not png_files:
        print(f"No PNG files found in '{input_path}'.")
        return

    print(f"Found {len(png_files)} PNG file(s).\n")

    for png_file in png_files:
        print(f"Processing: {png_file.name}")
        try:
            width, height, pixels, color_type, extra_chunks = decode_png(png_file.read_bytes())
        except Exception as e:
            print(f"  Skipped: {e}\n")
            continue

        channels = 3 if color_type == 2 else 4
        counts = replace_colors(pixels, channels, COLOR_PAIRS, TOLERANCE)

        any_changed = False
        for (old_color, new_color), count in zip(COLOR_PAIRS, counts):
            if count:
                print(f"  {old_color} → {new_color}  ({count} pixels)")
                any_changed = True
        if not any_changed:
            print("  No matching pixels found.")

        out_file = output_path / png_file.name
        out_file.write_bytes(encode_png(width, height, pixels, color_type, extra_chunks))
        print(f"  Saved → {out_file}\n")

    print("Done!")


if __name__ == "__main__":
    main()
