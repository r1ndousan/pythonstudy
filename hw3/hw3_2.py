from typing import List, Optional

def multiply_elements(elements: List[int], multiplier: Optional[int] = 2) -> List[int]:
    return [element * multiplier for element in elements]

multiply_lambda = lambda elements, multiplier=2: [element * multiplier for element in elements]

user_input = input("Введите список элементов через запятую: ")
elements = [int(x) for x in user_input.split(',')]
multiplier = int(input("Введите множитель (если не указан, будет умножено на 2): ") or 2)

result1 = multiply_elements(elements, multiplier)
result2 = multiply_lambda(elements, multiplier)
print(f"Функция с типизацией: {result1}\nЛямбда-функция:  {result2}")

