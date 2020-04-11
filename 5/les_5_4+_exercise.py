'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
'''

my_file2 = open("answer.txt", "w")

with open("text2.txt") as my_file1:
    for line in my_file1:
        if line.startswith('One'):
            print(line.replace('One', 'Один'), end='', file=my_file2)
        if line.startswith('Two'):
            print(line.replace('Two', 'Два'), end='', file=my_file2)
        if line.startswith('Three'):
            print(line.replace('Three', 'Три'), end='', file=my_file2)
        if line.startswith('Four'):
            print(line.replace('Four', 'Четыре'), end='', file=my_file2)
