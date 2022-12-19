

def choose_mode():
    return input('Введите режим работы : 1 - добавление записи, 2 - поиск')

def contact_to_s():
    return input('Введите информацию для поиска')

def new_contact():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
          
    return f'{last_name} || {first_name} || {phone_number}'

def show_found(result):
    print ('Результаты поиска: ')
    for i in result:
        print(i)
    
