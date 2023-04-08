

def delete():
    cont_delet = input("Введите данные контакта для удаления: ")
    with open('C:\\Users\\Евгений\\Desktop\\Python_Learn_1P\\Phonebook.txt', 'r', encoding='utf-8') as data:
        list_contact = data.readlines()
        for i_line in range(len(list_contact)):
            if cont_delet in list_contact[i_line]:
                del list_contact[i_line]
    with open('C:\\Users\\Евгений\\Desktop\\Python_Learn_1P\\Phonebook.txt', 'w', encoding='utf-8') as data_2:
        for line in list_contact:
            data_2.write(line)
