
def read_menu_number():
    menu_number_check = False
    menu_number = None
    while not menu_number_check:
        menu_number = input()
        if not menu_number.isdigit():
            print('Введите число!')
            continue
        menu_number = int(menu_number)
        if -1 < menu_number <= 6:
            menu_number_check = True
        else:
            print('Такого пункта нет!')
    return menu_number
