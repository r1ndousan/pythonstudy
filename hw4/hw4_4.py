def decorator(fibonacci):
    def wrapper(*args, **kwargs):
        comma = ', '.join(map(str, args))
        print(f"Функция {fibonacci.__name__} была вызвана с позиционными аргументами: ({comma}) и именованными аргументами: {kwargs}")
        return fibonacci(*args, **kwargs)
    return wrapper

@decorator
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 10
print(list(fibonacci(n)))