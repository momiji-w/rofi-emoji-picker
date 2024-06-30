xdotool type $(cat ./emoji_list.txt | rofi -dmenu -p 'Emoji 😊' -w $(xdo id) | awk '{ print $2 }')
