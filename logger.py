# from User_interface import get_info as gi
from os.path import exists
import csv
import file_creating
def add_new(contact):
    path = 'Phonebook.csv'
    path2 = 'Phonebook.txt'
    valid = exists(path)
    if not valid:
        file_creating.csv_creating()
    valid = exists(path2)
    if not valid:
        file_creating.txt_creating()
  
    with open ('Phonebook.txt', 'a', encoding = 'utf-8') as data:
            data.write(f'\n{contact}')
    with open ('Phonebook.csv', 'a',encoding = 'utf-8 ') as f:
            # f.write(f'\n{contact}')
            writer = csv.writer(f, delimiter=';')
            writer.writerows([contact.split(' || ')])
    
def get_base():
    with open ('Phonebook.txt', 'r', encoding = 'utf-8') as data:
        return data.read()
    # file = 'Phonebook.csv'
    # with open (file, 'a', encoding = 'utf-8') as data:

# info = gi()
# def writing_scv ():
#     file = 'Phonebook.csv'
#     with open (file, 'a', encoding = 'utf-8') as data:
#         data.write(f'{info[0]} ;{info[1]} ;{info[2]}\n')

# def writing_txt ():
#     file = 'Phonebook.txt'
#     with open (file, 'a', encoding = 'utf-8') as data:
#         data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\n\n')