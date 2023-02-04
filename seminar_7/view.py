


def main_menu():
    commands = [' показать все контакты',
                'Открыть файл',
                'Сохранить файл',
                'Новый контакт',
                'Изменить контакт',
                'Удалить контакт',
                'Найти контакт',
                'Выйти из программы']
    print('\nВыберите пункт меню: ')
    for i in range(len(commands)):
        print(f'\t{i+1}. {commands[i]}')
    user_input = int(input('\nВведите пункт меню: '))
    return user_input

def show_contacts(phone_book: list):
    if len(phone_book) > 0:
        for item in phone_book:
            print(f'{item[0]} {item[1]} ({item[2]})')
    else:
        print('Телефонная книга пустая или не загружена')

def load_success():
    print('Телефонная книга загружена успешно')

def save_success():
    print('Телефонная книга сохранена успешно')


def new_contact():
    name = input('введите имя и фамилию контакта: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий к контакту: ')
    return name, phone, comment

def change_success():
    print('Телефонная книга изменена успешно')

def delete_success():
    print('Запись удалена успешно')

def find_contact():
    search = input('введите искомое значение: ')
    return search

