from asyncio import constants

import view

path = 'phonebook.txt'
contacts = []


def read_file():
    global contacts
    with open(path) as f:
        contacts = [i.strip().split(':') for i in f.readlines()]
    return contacts


def get_contacts():
    global contacts
    with open(path, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line.strip())


def add_contact():
    global contacts
    id = input('Введите id: ')
    name = input('Введите Имя: ')
    phone = input('Введите номер: ')
    comment = input('Введите комментарий: ')
    contacts.append(f'{id}. {name} : {phone} : {comment}')
    with open(path, 'w', encoding='UTF-8') as f:
        for contact in contacts:
            f.writelines(str(contact + '\n'))


def rename_contact():
    global contacts
    while True:
        try:
            con1 = input('Какой контакт хотите изменить? ')
            break
        except ValueError:
            print('Введите имя контакта!')

    with open(path, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            if con1 in line:
                new = input('Введите новый контакт ')
                for i in contacts:
                    contacts[i] = new
                    with open(path, 'w', encoding='UTF-8') as fo:
                        fo.writelines((str(new + '\n')))



                # with open(path, 'a', encoding='UTF-8') as fo:
                #     id = input('Введите новое id: ')
                #     name = input('Введите новое Имя: ')
                #     phone = input('Введите новый номер: ')
                #     comment = input('Введите новый комментарий: ')
                #     contacts.append(f'{id}. {name} : {phone} : {comment}')
                #     for contact in contacts:
                #         fo.writelines((str(contact + '\n')))


def find_contact():
    while True:
        try:
            find = input('Какой контакт хотите найти? ')
            break
        except ValueError:
            print('Введите имя контакта!')

    with open(path, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            if find in line:
                print(line)
                break
            else:
                print('Такого контакта нет!')
                break


def delete_contact():
    while True:
        try:
            del_line = int(input('Выберите id контакта который хотите удалить? '))
            break
        except ValueError:
            print('Введите id контакта цифрой! ')
    with open(path, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    del lines[del_line]
    with open(path, 'w', encoding='UTF-8') as f:
        f.writelines(lines)


def save_file():
    global contacts
    with open(path, 'w', encoding='UTF-8') as f:
        for contact in contacts:
            f.writelines(str(contact + '\n'))


def exit_file():
    global contacts
    with open(path, 'w', encoding='UTF-8') as f:
        f.write(contacts)
