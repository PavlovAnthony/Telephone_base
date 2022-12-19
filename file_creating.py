def csv_creating ():
    file = 'Phonebook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия | Имя   | Номер телефона\n')
def txt_creating ():
    file2 = 'Phonebook.txt'
    with open (file2, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия | Имя    | Номер телефона\n')