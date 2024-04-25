# 1_2
num = int(input("Введите число: "))

for i in range(-num, num+1):
    print(i, end=' ')

sum_negative = 0
sum_positive = 0

for i in range(-num, num+1):
    if i < 0:
        sum_negative += i
    else:
        sum_positive += i

print("\nСумма отрицательных чисел:", sum_negative)
print("Сумма положительных чисел:", sum_positive)
