"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def read_change_symbols(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()                
        return text.replace('.', '!')


def write(text):
    with open('referat2.txt', 'w', encoding='utf-8') as f2:
        f2.write(text)


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    get_text = read_change_symbols('referat.txt')
    print('Symbols: ', len(get_text))
    print('Words: ', len(get_text.split()))
    write(get_text)


if __name__ == "__main__":
    main()
