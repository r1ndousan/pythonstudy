number_of_elements = int(input("Введите количество чисел в списке: "))
numbers = []

for i in range(number_of_elements):
    n = input(f"Введите число {i + 1}: ")
    numbers.append(n)

power = int(input("Введите степень: "))

for n in numbers:
    try:
        n = float(n)
        result = n ** power
    except ValueError:
        result = n * power
    print(f"{n} в степени {power} равно {result}")
