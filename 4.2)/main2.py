def divide_100_by(num):
    try:
        num = int(num)
        if num == 0:
            raise ZeroDivisionError
        result = 100 / num
        return result
    except ValueError:
        print("Ошибка: введено не число")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
print(divide_100_by(5))