''' 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''


def quantity_srt_word(nom_str, my_str):
    my_list = my_str.split()
    return print(f'в {nom_str}-ой строке {len(my_list)} слов')


with open("text.txt") as file_my:

    for i, line in enumerate(file_my, 1):
        quantity_srt_word(i, line)

print(f'всего строк: ', i)  # указывает что переменная локальная.. но так не хочется делать ей счетчик.. можно так?




