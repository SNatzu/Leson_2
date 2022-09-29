
contacts = {
    'ivan': '5553535',
    'petya': '88005553535',
    'vasya': '777-55-33'
}


def add_contact():
    name = input('Введите имя контакта')
    number = input('Введите номер телефона')
    contacts[name] = number


def show_contacts():
    print('-' * 35)
    for k, v in contacts.items():
        print(f'Имя: {k}, Номер: {v}')
    print('-' * 35)


def del_contact():
    name = input('Введите имя контакта для удаления: ')
    if contacts.get(name):
        contacts.pop(name)
        print('Контакт удален')
        print('-' * 35)
    else:
        print('Данного имени нет в тел.книге')


def find_contact():
    name = input('Введите имя нужного контакта: ')
    if contacts.get(name):
        print('-' * 35)
        print(f'Имя: {name}, Номер {contacts[name]}')
        print('-' * 35)
    else:
        print('Данного имени нет в тел.книге')


def save_contacts():
    with open('phonebook.txt', 'w', encoding='utf-8') as f:
        for k, v in contacts.items():
            f.write(f'{k}: {v}\n')
        print('Контакты сохранены в .txt')
        print('-' * 35)


def convert_contacts():
    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open('phonebook.csv', 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
        print('Контакты конвертированы в .csv')
        print('-' * 35)
