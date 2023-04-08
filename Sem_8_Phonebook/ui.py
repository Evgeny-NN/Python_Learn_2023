
import os
from logger import *
from load_data import load_data
from delete_data import delete
from edit_data import edit


def userinterfase():
    os.system('cls')
    print('''
1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - удалить контакт
6 - изменить контакт
7 - выход''')

    user_input = input('Введите нужный вариант: ')
    while user_input != '7':
        if user_input == '1':
            add_person()
        elif user_input == '2':
            search()
        elif user_input == '3':
            load_data()
        elif user_input == '4':
            print_data()
        elif user_input == '5':
            delete()
        elif user_input == '6':
            edit()
           
        else:
            print('Некорректный ввод, введите заново! ')
        os.system('cls')
        print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - удалить контакт
6 - изменить контакт
7 - выход''')
        user_input = input('Введите нужный вариант: ')
