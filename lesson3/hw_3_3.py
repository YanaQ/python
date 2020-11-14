# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))
def my_func(number_1, number_2, number_3):
    if number_1 <= number_2 and number_1 <= number_3:
        return number_2 + number_3
    elif number_2 <= number_1 and number_2 <= number_3:
        return number_1 + number_3
    else:
        return number_1 + number_2
print(my_func(number_1, number_2, number_3))

