
from create_data import *


def add_person():
    last_name = last_name_data()
    name = name_data()
    surname = surname_data()
    phone = phone_data()

    data = open('C:\\Users\\Евгений\\Desktop\\Python_Learn_1P\\Phonebook.txt',
                'a', encoding='utf-8')
    data.writelines([last_name, ' ',  name, ' ',  surname, ' ', phone, '\n'])
    data.close()


def print_data():
    with open('C:\\Users\\Евгений\\Desktop\\Python_Learn_1P\\Phonebook.txt', 'r', encoding='utf-8') as data:
        print(data.read())


def search():
    search_name = input('Введите данные абонента: ')
    with open('C:\\Users\\Евгений\\Desktop\\Python_Learn_1P\\Phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)
