# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


name = input('Введите свое имя: ')
surname = input('Введите свою фамилию: ')
year_of_birth = int(input('Введите год своего рождения: '))
mail = input('Введите свою электронную почту: ')
number = int(input('Введите свой номер телефона: '))
def information(name, surname, year_of_birth, mail, number):
    print(f"{name} {surname}, год рождения: {year_of_birth}, e-mail: {mail}, номер телефона: {number}")
information(name, surname, year_of_birth, mail, number)