# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем. Об окончании ввода данных свидетельствует пустая строка.
name = input('Ваше имя: ')
family = input('Ваша Фамилия: ')
age = input('Сколько вам лет: ')
content = open('hw_5_1.txt', 'w')
with content:
    content.write(name + '\n')
    content.write(family + '\n')
    content.write(age + '\n')
    content.close()
