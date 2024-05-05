# 1
squares = [x**2 for x in range(1, 11)]
print(squares)

# 2
weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
dict = {day: index+1 for index, day in enumerate(weekdays)}
print(dict)

# 3
tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
lowercase_tags = {tag.lower() for tag in tags}
print(lowercase_tags)
