import flet as ft
import sys

def main(page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def get_user_nickname():
        return txt_nickname.label

    def get_user_name():
        return txt_name.label

    def get_user_second_name():
        return txt_second_name.label

    def get_user_city():
        return txt_city.label

    def get_user_age():
        return txt_age.label

    def get_user_password():
        return txt_pasword.label

    def get_check_user_nickname():
        return txt_check_nickname.label

    def get_chack_user_password():
        return txt_check_pasword.label

    def start_registrat():
        return 1

    def start_ent():
        return 1

    def start_clos():
        return 1

    def button_clicked_enter1(e):
        get_user_nickname()
        get_user_name()
        get_user_second_name()
        get_user_city()
        get_user_age()
        get_user_password()
        start_registrat()
        page.update()

    def button_clicked_enter2(e):
        get_check_user_nickname()
        get_chack_user_password()
        start_ent()
        page.update()

    def button_clicked_start_registration(e):
        undel1()
        regist.visible = False
        login.visible = False
        close.visible = False
        page.update()

    def button_clicked_start_entry(e):
        regist.visible = False
        login.visible = False
        close.visible = False
        undel2()
        page.update()

    def button_clicked_start_close(e):
        regist.visible = False
        login.visible = False
        close.visible = False
        page.update()
        start_clos()
        sys.exit(404)

    def home(e):
        home1()
        del1()
        page.update()

    def del1():
        txt_nickname.visible = False
        txt_name.visible = False
        txt_second_name.visible = False
        txt_city.visible = False
        txt_age.visible = False
        txt_pasword.visible = False
        txt_check_nickname.visible = False
        txt_check_pasword.visible = False
        hom.visible = False
        enter1.visible = False
        enter2.visible = False
    def undel1():
        txt_nickname.visible = True
        txt_name.visible = True
        txt_second_name.visible = True
        txt_city.visible = True
        txt_age.visible = True
        txt_pasword.visible = True
        hom.visible = True
        enter1.visible = True
    def undel2():
        txt_check_nickname.visible = True
        txt_check_pasword.visible = True
        hom.visible = True
        enter2.visible = True

    def home1():
        regist.visible = True
        login.visible = True
        close.visible = True
        hom.visible = False

    txt_nickname = ft.TextField(value="", hint_text="Enter nickname", width=300)
    txt_name = ft.TextField(value="", hint_text="Enter your name", width=300)
    txt_second_name = ft.TextField(value="", hint_text="Enter your second name", width=300)
    txt_city = ft.TextField(value="", hint_text="Enter your city", width=300)
    txt_age = ft.TextField(value="", hint_text="Enter your age", width=300)
    txt_pasword = ft.TextField(value="", hint_text="Enter password", width=300)
    txt_check_nickname = ft.TextField(value="", hint_text="Enter nickname", width=300)
    txt_check_pasword = ft.TextField(value="", hint_text="Enter password", width=300)

    regist=ft.ElevatedButton(text="Registration",width=300, on_click=button_clicked_start_registration)
    login=ft.ElevatedButton(text="Login",width=300, on_click=button_clicked_start_entry)
    close=ft.ElevatedButton(text="Close",width=300, on_click=button_clicked_start_close)
    hom=ft.ElevatedButton(text="Back", on_click=home)
    enter1=ft.ElevatedButton(text="Enter", on_click=button_clicked_enter1)
    enter2=ft.ElevatedButton(text="Enter", on_click=button_clicked_enter2)
    i = 1
    if i == 1:
        del1()

    page.add(
        ft.Column(
            [
                regist,
                login,
                close,
                txt_nickname,
                txt_name,
                txt_second_name,
                txt_city,
                txt_age,
                txt_pasword,
                txt_check_nickname,
                txt_check_pasword,
                hom,
                enter1,
                enter2

            ],

        )
    )
ft.app(target=main)

