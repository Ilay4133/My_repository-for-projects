import sys
from model import entry_user, registration_new_user
from view import geting_user_nickname, geting_user_name, geting_user_second_name, geting_user_city,geting_user_age, geting_user_password, geting_check_user_nickname,geting_chack_user_password, start_registrating, start_enting, start_closing

def start_registration():
    user_nickname = geting_user_nickname
    user_name = geting_user_name
    user_second_name = geting_user_second_name
    user_city = geting_user_city
    user_age = geting_user_age
    user_password = geting_user_password
    registration_new_user(user_nickname, user_name, user_second_name, user_city, user_age, user_password)

def start_entry():
    check_user_nickname =  geting_check_user_nickname()
    chack_user_password = geting_chack_user_password()
    entry_user(check_user_nickname, chack_user_password)

def start_close():
    sys.exit(404)


def start_code():
    while True:
        if start_registrating == 1:
            start_registration()
            break
        elif start_enting() == 1:
            start_entry()
            break
        elif start_closing() == 1:
            start_close()
            break

