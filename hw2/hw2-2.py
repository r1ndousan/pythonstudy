user_input = input("Введите строку: ")
user_input = user_input.lower()

char_count = {}
for char in user_input:
    if char != " ":
        count = user_input.count(char)
        char_count[char] = count

print(char_count)
