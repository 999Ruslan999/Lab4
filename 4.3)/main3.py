def is_magical_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        last_two_digits = year % 100
        if day * month == last_two_digits:
            return True
        else:
            return False
    except ValueError:
        print("Ошибка: неверный формат даты")
        return False
print(is_magical_date("30.02.2021"))