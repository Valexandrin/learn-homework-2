"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta #lib. arrow


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = datetime.now()
    print('Today: ', today)

    print('Yesterday: ',today - timedelta(days=1))
    
    print('30 days ago: ',today - timedelta(days=30))


def main():
    print_days()
    print(datetime.strptime('01/01/20 12:10:03.234567', '%y/%m/%d %H:%M:%S.%f'))


if __name__ == "__main__":
    main()