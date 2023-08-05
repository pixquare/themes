# How to contribute
If you have create a beautiful theme and want to share it with others. The easiest way is to submit a pull request to this repo, so that everyone can download and use your theme.

By this time, you should already know about the theme structure, but if you still need more info on that topic, you can check it again [here](./theme_structure.md)

## Packaging
Before submitting the theme, we'll need to bundle the theme into a `zip` file first. Simply compress the components of your theme into a zip. Note that we need to compress the components directly instead of the folder that contain those components.

Name that `zip` file `Theme.zip` then place it a folder with the name of your theme

## Submitting the PR
For those who are familiar with Git system, you can submit a pull request to this repo. I'll review it and merge it as soon as possible. If for some reason, I don't seem to be active on your pull request, please ping me in [Discord](https://discord.gg/5stJz4cDGM) or shoot an email to `info@pixquare.art`.

In the PR, you also need to update the `themes.json` file in this repo's root. The new object should be exactly the same as the content of your theme `info.json`.

## Submitting it somewhere else
If you have not worked with Git before, you can contact me in [Discord](https://discord.gg/5stJz4cDGM) or shoot me an email at `info@pixquare.art`. I'll check the theme and add it to the repo.

## Updating your theme
As Pixquare continues to evolve, it will add more images to the list. So you might need to update your theme to accommondate for the new assets. To do that, after adding the new assets to your theme, you'll need to bump the version number in the `info.json` of your theme and the `themes.info` of the main repo.


Thank you
