# rofi-emoji-picker
Emoji picker script for rofi.
## Get started
### Required applications
- [rofi](https://github.com/davatorium/rofi)
- [xdo](https://github.com/baskerville/xdo)
- [awk](https://github.com/onetrueawk/awk)

### Clone the repo
```shell
git clone https://github.com/momiji-w/rofi-emoji-picker.git
cd rofi-emoji-picker
```
### Change permissions of the script
```shell
chmod +x script.sh
```
### Run the script
```shell
./script.sh
```
## Using with Desktop environment
### Example with awesomewm
adding shortcut key to the config (super + '.' in this example).
```lua
awful.key({ modkey }, ".",
  function()
    awful.spawn.with_shell(
      "xdotool type $(cat ~/.local/share/emoji_list.txt | rofi -dmenu -p 'Emoji 😊' -w $(xdo id) | awk '{ print $2 }')")
  end,
  { description = "emoji picker", group = "client" }
)
```
edit the location of the emoji list to the desired location.
## For Wayland Users
Wayland users can replace the tools used the here with [wofi](https://hg.sr.ht/~scoopta/wofi) and [wtype](https://github.com/atx/wtype).
### Example with Hyprland
```config
$emoji = wtype $(cat ~/.local/share/emoji_list.txt | wofi -S dmenu -p 'Emoji:' | awk '{ print $2 }')
bind = $mainMod, B, exec, $emoji
```
## Credits
shout out to [BuonOmo](https://gist.github.com/BuonOmo/77b75349c517defb01ef1097e72227af) for their list of UTF-8 emoji list.
