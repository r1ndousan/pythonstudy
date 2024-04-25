num = input("Введите трехзначное число, в котором все цифры различны: ")

if len(num) != 3 or not num.isdigit() or len(set(num)) != 3:
    print("Пожалуйста, введите трехзначное число с различными цифрами.")
else:
    permutations = [int(num[0] + num[1] + num[2]), int(num[0] + num[2] + num[1]),
                    int(num[1] + num[0] + num[2]), int(num[1] + num[2] + num[0]),
                    int(num[2] + num[0] + num[1]), int(num[2] + num[1] + num[0])]

    print("Числа, образованные при перестановке цифр:", permutations)