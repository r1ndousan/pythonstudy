while True:
    input_value = input("Введите число или 'exit' для выхода: ")

    if input_value == "exit":
        break
    try:
        number = int(input_value)
    except ValueError:

        print("Введите именно число.")
        continue

    print(f"Длина числа: {len(str(number))}")