
UI_ITEMS = [
    '1. Добавить контакт',
    '2. Отобразить контакты',
    '3. Поиск контакта (по имени)',
    '4. Удалить контакт',
    '5. Сохранить контакты в .txt',
    '6. Экспортировать в .csv',
    '0. Выход'
]


def show_user_interface():
    for item in UI_ITEMS:
        print(item)
    print('Введите пункт меню')