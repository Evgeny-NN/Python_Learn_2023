
def edit():
    
    cont_edit = input("Введите контакт для изменения: ")
    last_name = input("Введите новое фамилие: ")
    name = input("Введите новое имя: ")
    surname = input("Введите новое отчество: ")
    phone = input("Введите новый номер телефона: ")
    with open('C:\\Users\\Евгений\\Desktop\\Python_Learn_1P\\Phonebook.txt', 'r', encoding='utf-8') as data:
        list_contact = data.readlines()
        for i_line in range(len(list_contact)):
            if cont_edit in list_contact[i_line]:
                list_contact[i_line] = last_name + '' + name + '' + surname + '' + phone
    with open('C:\\Users\\Евгений\\Desktop\\Python_Learn_1P\\Phonebook.txt', 'w', encoding='utf-8') as data_2:
        for line in list_contact:
            data_2.write(line)
            