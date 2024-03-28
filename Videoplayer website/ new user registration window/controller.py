import sys
from model import entry_user, registration_new_user
from view import get_user_nickname, get_user_name, get_user_second_name, get_user_city,get_user_age, get_user_password, get_check_user_nickname,get_chack_user_password, start_registrat, start_ent, start_clos

from view import main().__import__(get_user_nickname)

def start_code():
    while True:
        if start_registrat() == 1:
            start_registration()
            break
        elif start_ent() == 1:
            start_entry()
            break
        elif start_clos() == 1:
            start_close()
            break
def start_registration():
    user_nickname = get_user_nickname()
    user_name = get_user_name()
    user_second_name = get_user_second_name()
    user_city = get_user_city()
    user_age = get_user_age()
    user_password = get_user_password()
    registration_new_user(user_nickname, user_name, user_second_name, user_city, user_age, user_password)


def start_entry():
    check_user_nickname =  get_check_user_nickname()
    chack_user_password = get_chack_user_password()
    entry_user(check_user_nickname, chack_user_password)


def start_close():
    sys.exit(404)

