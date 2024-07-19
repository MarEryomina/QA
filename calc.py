start = input('Запустить калькулятор - 1, завершить - 0')
while start != '0':
    try:
        num1 = int(input('Введите 1 число:'))
        operator = input('Арифметический знак, один из: +, -, *, /')
        num2 = int(input('Введите 2 число:'))
        if operator == '+':
            result = num1 +num2
            print('Результат:', result)
        elif operator == '-':
            result = num1 - num2
            print('Результат:', result)
        elif operator == '*':
            result = num1 * num2
            print('Результат:', result)
        elif operator == '/':
            try:
                result = num1 / num2
                print('Результат:', result)
            except:
                print('На 0 делить нельзя!')
        else:
            print('Неверно введено действие!')
    except:
        print('Неверно введены числа!')
    start = input('Запустить калькулятор - 1, завершить - 0')