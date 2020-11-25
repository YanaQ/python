# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами
# . Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
def summary():
    try:
        with open('hw_5_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел: ')
            file_obj.writelines(line)
            my_numb = line.split()
            print(f'Сумма введенных цифр: {sum(map(int, my_numb))}')
    except IOError:
        print('Ошибка в файле')

    except ValueError:
        print('Неправильно введен символ. Ошибка ввода-вывода')
summary()