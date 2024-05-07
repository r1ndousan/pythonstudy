def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)

# среднее значение
assert average_num([1, 2, 3, 4, 5]) == 3.0
assert average_num([1.5, 2.5, 3.5]) == 2.5

# строка вместо чисел
assert average_num([1, 'a', 3]) == "Bad request"

# нули в списке
assert average_num([0, 0, 0, 0]) == 0.0

# один элемент
assert average_num([10]) == 10.0

# отрицательные значения
assert average_num([-1, -2, -3, -4]) == -2.5

# большое количество элементов
assert average_num(list(range(100))) == 49.5

# целые и нецелые числа (будет ошибка)
assert average_num([1, 2.5, 3, 4.5]) == 4.0

