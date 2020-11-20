# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
# строк, количества слов в каждой строке.
with open('hw_5_2.txt', 'r') as file_obj:
    lines = 1
    for line in file_obj:
        lines += line.count('\n')
    print(f'Количество строк: {lines}')
with open('hw_5_2.txt', 'r') as my_file:
    number = 0
    for number, item in enumerate(my_file, 1):
        letters = item.split(' ')
        print(f'Количество слов в строке {number}: {len(letters)}')


