class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return x / y

    def power(self, x, y):
        return x ** y

def main():
    calculator = Calculator()

    while True:
        operation = input("Введите операцию (+, -, *, /, ** - возведение в степень, q - выход): ")

        if operation == 'q':
            print("Завершение программы...")
            break

        if operation not in ['+', '-', '*', '/', '**']:
            print("Неверная операция. Пожалуйста, попробуйте снова.")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите корректные числа.")
            continue

        if operation == '+':
            result = calculator.add(num1, num2)
        elif operation == '-':
            result = calculator.subtract(num1, num2)
        elif operation == '*':
            result = calculator.multiply(num1, num2)
        elif operation == '/':
            try:
                result = calculator.divide(num1, num2)
            except ZeroDivisionError as e:
                print(e)
                continue
        elif operation == '**':
            result = calculator.power(num1, num2)

        print(f"Результат: {result}")

if __name__ == "__main__":
    main()
