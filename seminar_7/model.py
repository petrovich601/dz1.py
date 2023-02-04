import controller
import view
phone_book = []
# result = []

path = 'seminar_7/phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book


def update_phone_book(contact: list):
    global phone_book
    phone_book.append(contact)


def open_phone_book():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))


def save_phone_book():
    global phone_book
    global path
    data = []
    for line in phone_book:
        data.append(';'.join(line))
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))


def search_contact(search: str):
    global phone_book
    search_results = []
    for line in phone_book:
        for field in line:
            if search in field:
                search_results.append(line)
                break
    return search_results


def delete_line_in_book(res):
    global phone_book
    global path
    temp_book = []
    data = []
    for line in phone_book:
        if res != line:
            temp_book.append(line)
    phone_book = temp_book
    for line in temp_book:
        data.append(';'.join(line))
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))
            

def change_phone_book(res, new):
    global phone_book
    global path
    temp_book = []
    data = []
    for line in phone_book:
        if res != line:
            temp_book.append(line)
        else:
            temp_book.append(new)
    phone_book = temp_book
    for line in temp_book:
        data.append(';'.join(line))
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))