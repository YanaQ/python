#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки
# типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не
# запрашивать у пользователя, а указать явно, в программе.

number = 10
number_dot = 12.4
text = 'the weather is wonderful'
my_cortege = (3, 'cat')

big_list = [number, number_dot, text, my_cortege]
for i in big_list:
    print(f'{i} is {type(i)}')


