import math

def calculator():
    try:
        operation = input("Введите операцию (+, -, *, /, **, sqrt, !, sin, cos, tan): ")
        
        if operation in ['+', '-', '*', '/', '**']:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            if operation == '/' and num2 == 0:
                print("Ошибка: деление на 0.")
            else:
                if operation == '+':
                    print("Результат:", num1 + num2)
                elif operation == '-':
                    print("Результат:", num1 - num2)
                elif operation == '*':
                    print("Результат:", num1 * num2)
                elif operation == '/':
                    print("Результат:", num1 / num2)
                elif operation == '**':
                    print("Результат:", num1 ** num2)
        elif operation == 'sqrt':
            num = float(input("Введите число: "))
            if num < 0:
                print("Ошибка: квадратный корень из отрицательного числа.")
            else:
                print("Результат:", math.sqrt(num))
        elif operation == '!':
            num = int(input("Введите целое неотрицательное число: "))
            if num < 0:
                print("Ошибка: факториал отрицательного числа.")
            else:
                print("Результат:", math.factorial(num))
        elif operation in ['sin', 'cos', 'tan']:
            angle = float(input("Введите угол в градусах: "))
            if operation == 'sin':
                print("Результат:", math.sin(math.radians(angle)))
            elif operation == 'cos':
                print("Результат:", math.cos(math.radians(angle)))
            elif operation == 'tan':
                print("Результат:", math.tan(math.radians(angle)))
        else:
            print("Ошибка: Неподдерживаемая операция.")
    except ValueError:
        print("Ошибка: Неверный формат числа.")
    except Exception as e:
        print("Ошибка:", e)

calculator()