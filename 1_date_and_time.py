"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    td = datetime.now()
    print('Today: ', td)

    delta = timedelta(days=1)
    ytd = td - delta
    print('Yesterday: ',ytd)

    delta = timedelta(days=30)
    ytd = td - delta
    print('30 days ago: ',ytd)


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    s_convert = datetime.strptime(date_string, '%y/%m/%d %H:%M:%S.%f')
    return s_convert


def main():
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))


if __name__ == "__main__":
    main()