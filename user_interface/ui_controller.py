from .ui_view import show_user_interface
from .ui_input import read_menu_number
from models import models as m


def start():
    menu_number = 1
    while menu_number != 0:
        show_user_interface()
        menu_number = read_menu_number()
        if menu_number == 1:
            m.add_contact()
        if menu_number == 2:
            m.show_contacts()
        elif menu_number == 3:
            m.find_contact()
        elif menu_number == 4:
            m.del_contact()
        elif menu_number == 5:
            m.save_contacts()
        elif menu_number == 6:
            m.convert_contacts()
