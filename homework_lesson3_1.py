def div(*args):

    try:
        arg1 = int(input("Введите число "))
        arg2 = int(input("Введите второе число "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Вы не можете делить на ноль"

    return res

print(f'result  {div()}')
