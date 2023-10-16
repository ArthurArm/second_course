first = input()
second = input()
last_printed = first

for character_index in range(len(first)):
    left_part = second[0:character_index + 1]
    right_part = first[character_index + 1:]
    new = left_part + right_part
    if new != last_printed:
        print(new)
        last_printed = new
