txt = open("buonomo_emoji_list.txt").read().split("\n")

new_lines = []
for line in txt:
    split_line = line.split("=")

    if len(split_line) < 2:
        continue

    emoji_name = split_line[0][6::]
    emoji = split_line[1]
    new_lines.append(f"{emoji_name} {emoji}")

with open("emoji_list.txt", "w") as f:
    f.write("\n".join(new_lines))
