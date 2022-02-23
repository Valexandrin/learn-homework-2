"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def reader(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        length = len(text.split())
        text = text.replace('.', '!')
        return text


def writer(text):
    with open('referat2.txt', 'w', encoding='utf-8') as f2:
        f2.write(text)


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    get_text = reader('referat.txt')
    writer(get_text)                    


if __name__ == "__main__":
    main()
