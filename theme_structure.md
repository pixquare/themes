# Pixquare theme structure
This guide is only for those who want to custom their theme and/or contribute to the list of pre-built themes so other users can download and use. If you are planning to only use pre-built themes. You can skip this guide and go to [How to use](./how_to_use.md).

### Folder structure
When you inspect the files of Pixquare in Files app, you'll see a folder called `themes`. In there, you will find a list of available themes (either downloaded or created by you) that you can apply in Pixquare. Each folder contains a theme and will have this structure:
```
- Theme-name (1)
  `- "colors.json" (optional, file) (2)
  `- "images" (optional, folder) (3)
    `- all the png icon files, doesn't need to have all (4)
  `- "font" (optional, folder) (5)
    `- a single font file (6)
  `- "info.json" (7) (required in most cases)
```
    
Pixquare theme consist of 3 elements: colors, images, and font. When you create a custom theme, you can supply all of them or only 1 of them.

Here are the explanation for each file/folder:
 - (1) A container foler with your theme's name, if you want to contribute your theme to the list of this repo, you'll need to make sure the name is not used. 
   - Theme name cannot be `Default`. If planned to contribute to this repo, the name can not be `Custom` either.
   - Theme name can only have alpha-numeric characters.
   - `Custom` is a special theme name. It doesn't require the `info.json`. This is where you will store your custom theme for local use. When you edit colors in Pixquare theme settings, this folder will be created with the `colors.json`. You can also create this folder manually. Other elements can be added to this to acts as a normal theme.
  - (2) This is where you'll store the colors info for the theme. Take a look at (\*) for the template.
  - (3) This is where you'll store the images for the theme.
  - (4) Images has to be `png` format. Take a look at (\*\*) for the list of images name
    - The default images for Pixquare that I design are only 16x16, but you can increase that to make them as high-res as you want, however, I recommend to keep them 128x128 or below. Going beyond that doesn't really change anything.
    - You only need to supply as many images as you need, if an image is not supplied, it will simply use the default one.
  - (5) This where you'll store your font
  - (6) The font file, can be named anything, if you put multiple files in here, only the first one is used.
  - (7) All them excpt `Custom` is required to have this file, otherwise, Pixquare will not register the theme as valid. The structure of the theme is as the following:
```
{
  "name": <theme name>,
  "author": <your name>,
  "desc": <a short desription of your theme>,
  "versionNumber": <an integer, this is to compare and see if the them can be update>,
  "availableAssets": <an array of strings, available values are "colors", "images", and "font">
}
```
  
  As an example for (1), (3), and (7), you can take a look at the default [Dark](./Dark) theme in this repo as the reference. I will make sure that this theme will have all the images available in Pixquare.
  
  \* **color.json template**
  ```
  {
  "primary": <color>,
  "secondary": <color>,
  "primaryText": <color>,
  "secondaryText": <color>,
  "highlightText": <color>,
  "selectedText": <color>,
  "background": <color>,
  "secondaryBackground": <color>,
  "highlightBackground": <color>,
  "selectedBackground": <color>,
  "canvasBackground": <color>,
  "emphasizedBackground": <color>,
  "primaryButton": <color>,
  "secondaryButton": <color>
}

Each <color> is this:
{
  "hue": <0-1>,
  "value": <0-1>
  "saturation": <0-1>,
  "alpha": <0-1>
}
```

\*\* **All images files** (images added later will be at the bottom)
```
checkbox_box.png
checkbox_check_mark.png
ic_canvas_resize_bottom.png
ic_canvas_resize_bottom_left.png
ic_canvas_resize_bottom_right.png
ic_canvas_resize_center.png
ic_canvas_resize_left.png
ic_canvas_resize_right.png
ic_canvas_resize_top.png
ic_canvas_resize_top_left.png
ic_canvas_resize_top_right.png
ic_color_palette_clear.png
ic_color_palette_gradient.png
ic_color_palette_lospec.png
ic_color_palette_open.png
ic_color_palette_save.png
ic_color_palette_search.png
ic_contextual_alpha_lock.png
ic_contextual_blend_mode.png
ic_contextual_clear.png
ic_contextual_clear_clipboard.png
ic_contextual_clipboard_more.png
ic_contextual_convert.png
ic_contextual_copy.png
ic_contextual_cut.png
ic_contextual_deselect.png
ic_contextual_duration.png
ic_contextual_entry_options.png
ic_contextual_flip_horizontal.png
ic_contextual_flip_vertical.png
ic_contextual_frame_more.png
ic_contextual_invert_select.png
ic_contextual_link.png
ic_contextual_merge.png
ic_contextual_opacity.png
ic_contextual_original_size.png
ic_contextual_paste.png
ic_contextual_rename.png
ic_contextual_selection_more.png
ic_contextual_unlink.png
ic_gallery_browser_add_new.png
ic_gallery_browser_artwork.png
ic_gallery_browser_back.png
ic_gallery_browser_copy.png
ic_gallery_browser_cut.png
ic_gallery_browser_delete.png
ic_gallery_browser_export.png
ic_gallery_browser_folder.png
ic_gallery_browser_gear.png
ic_gallery_browser_import.png
ic_gallery_browser_logo.png
ic_gallery_browser_rename.png
ic_gallery_browser_settings_icon.png
ic_gallery_browser_settings_list.png
ic_gallery_browser_share.png
ic_gallery_browser_theme.png
ic_gesture_pad_swipe_arrow.png
ic_layer_selector_add_reference_layer.png
ic_layer_selector_blend_mode.png
ic_layer_selector_both_linked.png
ic_layer_selector_folder_add.png
ic_layer_selector_folder_closed.png
ic_layer_selector_folder_open.png
ic_layer_selector_frame.png
ic_layer_selector_frame_add.png
ic_layer_selector_frame_duplicate.png
ic_layer_selector_frame_empty.png
ic_layer_selector_frame_options.png
ic_layer_selector_frame_remove.png
ic_layer_selector_invisible.png
ic_layer_selector_last.png
ic_layer_selector_layer_add.png
ic_layer_selector_layer_duplicate.png
ic_layer_selector_layer_options.png
ic_layer_selector_layer_remove.png
ic_layer_selector_leading_linked.png
ic_layer_selector_linked.png
ic_layer_selector_locked.png
ic_layer_selector_next.png
ic_layer_selector_onion_skin_off.png
ic_layer_selector_onion_skin_on.png
ic_layer_selector_pause.png
ic_layer_selector_play.png
ic_layer_selector_reference_layer.png
ic_layer_selector_trailing_linked.png
ic_layer_selector_unlinked.png
ic_layer_selector_unlocked.png
ic_layer_selector_visible.png
ic_menu_back.png
ic_menu_canvas_rotate.png
ic_menu_export.png
ic_menu_eye_dropper.png
ic_menu_gear.png
ic_menu_gesture.png
ic_menu_grid.png
ic_menu_left_hand_mode.png
ic_menu_paste.png
ic_menu_pen_tip.png
ic_menu_pencil.png
ic_menu_reference_image.png
ic_menu_resize.png
ic_menu_save.png
ic_menu_symmetry.png
ic_misc_3_dots.png
ic_misc_add.png
ic_misc_arrow.png
ic_misc_big_arrow.png
ic_misc_big_x.png
ic_misc_check_mark.png
ic_misc_double_arrow.png
ic_misc_drag_knob.png
ic_misc_dropdown.png
ic_misc_files.png
ic_misc_info.png
ic_misc_photos.png
ic_misc_remove.png
ic_misc_small_x.png
ic_preview.png
ic_preview_close.png
ic_preview_pause.png
ic_preview_play.png
ic_preview_resize.png
ic_quick_actions_redo.png
ic_quick_actions_undo.png
ic_reference_image.png
ic_reference_image_dismiss.png
ic_reference_image_edit.png
ic_reference_image_resize.png
ic_social_discord.png
ic_social_email.png
ic_social_link.png
ic_social_rate.png
ic_symmetry.png
ic_tool_angle.png
ic_tool_brush.png
ic_tool_circle.png
ic_tool_color_bucket.png
ic_tool_color_replace.png
ic_tool_contiguous.png
ic_tool_curve.png
ic_tool_dither_2x2.png
ic_tool_dither_4x4.png
ic_tool_dither_8x8.png
ic_tool_eraser.png
ic_tool_eye_dropper.png
ic_tool_fill.png
ic_tool_line.png
ic_tool_linear_gradient.png
ic_tool_more.png
ic_tool_move.png
ic_tool_pixel_perfect.png
ic_tool_pressure_sensitivity.png
ic_tool_radial_gradient.png
ic_tool_ratio.png
ic_tool_rectangle.png
ic_tool_round_tip.png
ic_tool_selection_add.png
ic_tool_selection_box.png
ic_tool_selection_circle.png
ic_tool_selection_intersect.png
ic_tool_selection_lasso.png
ic_tool_selection_magic_wand.png
ic_tool_selection_polygon.png
ic_tool_selection_replace.png
ic_tool_selection_subtract.png
ic_tool_selection_xor.png
ic_tool_square_tip.png
ic_tool_stroke_type.png
ic_tool_water_color.png
misc_circle_frame.png
misc_icon_frame.png
pull_tab_arrow_horizontal.png
pull_tab_arrow_vertical.png
pull_tab_background_horizontal.png
pull_tab_background_vertical.png
slider_bar_bottom.png
slider_bar_middle.png
slider_bar_top.png
slider_knob.png
toggle_knob.png
toggle_left_off.png
toggle_left_on.png
toggle_right_off.png
toggle_right_on.png

--- v1.8 ---
ic_gallery_browser_settings_sort

--- v1.9 ---
ic_common_import
ic_common_artwork
--- v1.10 ---
ic_menu_guide_line
ic_gallery_browser_settings_tips
--- v1.11 ---
ic_color_palette_shading
ic_menu_language
--- v1.12 ---
ic_contextual_clipping_mask
ic_contextual_cropping_mask
ic_layer_selector_clipping_mask
ic_layer_selector_cropping_mask
ic_layer_selector_animation_drag
ic_menu_label
ic_menu_snapping
--- v1.13 ---
ic_contextual_mask
ic_tool_color_adjustment
--- v2.0.0 ---
ic_freemium_full_access
ic_freemium_tip
--- v2.1.0 ---
ic_preview_center
--- v2.2.0
ic_tool_outline
--- v2.3.0 ---
ic_tool_contour
--- v2.4.0 ---
ic_gallery_browser_settings_icloud
ic_gallery_browser_settings_on_device
ic_menu_zoom
--- v2.5.0 ---
ic_contextual_tag
--- v2.6.0 ---
ic_layer_selector_add_tilemap_layer
ic_tileset_add
ic_tileset_remove
ic_tileset
--- v2.7.0 ---
ic_tool_blur_tip
ic_tool_jumble_tip
ic_tool_spray_tip
ic_tool_spray_with_opacity_tip
submenu_path_bottom
submenu_path_middle
--- v2.10.0 ---
ic_tool_custom_objects
--- v2.11.0 ---
handy_joystick_black_white
handy_joystick_knob
ic_menu_looping
ic_tool_dither_noise
submenu_path_straight
--- v2.12.0 ---
ic_preview_navigation
ic_multi_tab
ic_multi_tab_expand
ic_multi_tab_collapse
ic_multi_tab_unsaved
ic_info_coordinate
ic_info_origin
ic_info_size
--- v2.16.0 ---
ic_misc_refresh
--- v2.23.0 ---
ic_menu_fun
--- v2.45.0 ---
ic_tool_stabilizer
ic_common_swap
--- v2.47.0 ---
ic_tool_post_processing
--- v2.48.0 ---
ic_tileset_duplicate
```
