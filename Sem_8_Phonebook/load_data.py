
def load_data():
    with open('C:\\Users\\Евгений\\Desktop\\Python_learn\\HomeWork_8_Tel_Book\\Phonebook.txt', 'r+', encoding='utf-8') as data:
        text_data = data.read()
        path = input('Введите адрес файла: ')
        with open(path, 'r', encoding='utf-8') as data_2:
            for line in data_2:
                if line not in text_data:
                    data.write(line)