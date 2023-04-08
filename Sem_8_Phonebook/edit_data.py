from logger import search
from create_data import *

def edit():
    
    cont_edit = input("Введите контакт для изменения: ")
    last_name = input("Введите новое фамилие: ")
    name = input("Введите новое имя: ")
    surname = input("Введите новое отчество: ")
    phone = input("Введите новый номер телефона: ")
    with open('C:\\Users\\Евгений\\Desktop\\Python_learn\\HomeWork_8_Tel_Book\\Phonebook.txt', 'r', encoding='utf-8') as data:
        list_contact = data.readlines()
        for i_line in range(len(list_contact)):
            if cont_edit in list_contact[i_line]:
                list_contact[i_line] = last_name + '' + name + '' + surname + '' + phone
    with open('C:\\Users\\Евгений\\Desktop\\Python_learn\\HomeWork_8_Tel_Book\\Phonebook.txt', 'w', encoding='utf-8') as data_2:
        for line in list_contact:
            data_2.write(line)
    # with open('C:\\Users\\Евгений\\Desktop\\Python_learn\\HomeWork_8_Tel_Book\\Phonebook.txt', 'r', encoding='utf-8') as data:
    #     list_contact = data.readlines()
    #     print('Какое поле вы хотите изменить?')
    #     field = input('1 - Фамилия\n2 - Имя\n3 - Отчество\n4 - Номер телефона\n')
    #     if field == '1':
    #         cont_edit[0] = input('Введите фамилию: ')
    #     elif field == '2':
    #         cont_edit[1] = input('Введите имя: ')
    #     elif field == '3':
    #         cont_edit[2] = input('Введите отчество: ')
    #     elif field == '4':
    #         cont_edit[3] = input('Введите номер телефона: ')
    #     list_contact.append(cont_edit)
    # with open('C:\\Users\\Евгений\\Desktop\\Python_learn\\HomeWork_8_Tel_Book\\Phonebook.txt', 'w', encoding='utf-8') as data_2:
    #     for line in list_contact:
    #         # line = ' '.join(line) + '\n'
    #         # if cont_delet in line:
    #         data_2.write(line)
          