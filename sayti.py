import os

urls = [
    ('https://www.youtube.com/', 'Youtube'),
    ('https://www.pivo.com/', 'Сайт для пива'),
    ('https://fentezi.by/', 'Продажа дилдо'),
    ('https://habr.com/ru/all/', 'Хабр'),
    ]

url_names = '\n'.join((f' {i + 1}. {url_name}.' for i, (_, url_name) in enumerate(urls)))

def main():
    slava = input(f'Привет! Что хочешь открыть ?\n{url_names}\nТвой выбор: ')

    try:
        url_num = int(slava) - 1
        os.system ('start ' + urls[url_num][0])
    except:
        print('Допустимые значения: 1 -', len(urls))

if __name__ == '__main__':
    main()
