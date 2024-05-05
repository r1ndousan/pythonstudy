def texting(text, name):
    with open(name, mode='a+') as file:
        file.write(text + '\n')

    with open(name, mode='r') as file:
        lines = file.readlines()
        print("Информация из четных строк файла:")
        for index in range(1, len(lines), 2):
            print(lines[index].strip())

text_to_write = "Первая строка\nВторая строка\nТретья строка\nЧетвертая строка\n"
name = "hw4_3_1.txt"
texting(text_to_write, name)
