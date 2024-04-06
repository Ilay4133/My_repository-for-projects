import flet as ft
import sys

rer1=""
rer2=""
open('Users_DATA_File.txt', 'a').close()

def main(page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode=""

    def registration_new_user():
        Users_DATA_File = open("Users_DATA_File.txt", "a+")
        Users_DATA_File.write("User: \n")
        Users_DATA_File.write(f"{geting_user_nickname}\n")
        Users_DATA_File.write(f"{geting_user_name}\n")
        Users_DATA_File.write(f"{geting_user_second_name}\n")
        Users_DATA_File.write(f"{geting_user_city}\n")
        Users_DATA_File.write(f"{geting_user_age}\n")
        Users_DATA_File.write(f"{geting_user_password}\n")
        Users_DATA_File.write("_\n")
        Users_DATA_File.close()

    def entry_user():
        print(geting_check_user_nickname)
        print(geting_check_user_password)
        with open("Users_DATA_File.txt") as f:
            lines = f.readlines()  # прочитать файл построчно в списко

        for line in lines:
            if geting_check_user_nickname == line[:-1]:  # [:-1] - все символы, кроме последнего, который перевод строки
                print(True)
                for line in lines:
                    if geting_check_user_password == line[:-1]:  # [:-1] - все символы, кроме последнего, который перевод строки
                        print(True)
                        print(2)
                        return 2
                    else:
                        print(1)
                        print(False)
                        yield 1
            else:
                print(0)
                print(False)
                yield 0



    def get_user_nickname():
        global geting_user_nickname
        geting_user_nickname=txt_nickname.value
        return geting_user_nickname

    def get_user_name():
        global geting_user_name
        geting_user_name=txt_name.value
        return geting_user_name

    def get_user_second_name():
        global geting_user_second_name
        geting_user_second_name=txt_second_name.value
        return geting_user_second_name

    def get_user_city():
        global geting_user_city
        geting_user_city=txt_city.value
        return geting_user_city

    def get_user_age():
        global geting_user_age
        geting_user_age=txt_age.value
        return geting_user_age

    def get_user_password():
        global geting_user_password
        geting_user_password=txt_pasword.value
        return geting_user_password

    def get_check_user_nickname():
        global geting_check_user_nickname
        geting_check_user_nickname=txt_check_nickname.value
        return geting_check_user_nickname

    def get_chack_user_password():
        global geting_check_user_password
        geting_check_user_password=txt_check_pasword.value
        return geting_check_user_password

    def button_clicked_enter1(e):
        get_user_nickname()
        get_user_name()
        get_user_second_name()
        get_user_city()
        get_user_age()
        get_user_password()
        registration_new_user()
        txt_nickname.value=""
        txt_name.value=""
        txt_second_name.value=""
        txt_city.value=""
        txt_age.value=""
        del1()
        txt_registration.visible=True
        Ok1.visible = True
        page.update()

    def button_clicked_enter2(e):
        get_check_user_nickname()
        get_chack_user_password()
        entry_user()
        del1()
        txt_registration.visible = True
        Ok1.visible = True
        del1()
        txt_entry.visible = True
        Ok2.visible = True
        page.update()

    def button_clicked_ok1(e):
        home1()
        txt_registration.visible=False
        Ok1.visible = False
        page.update()

    def button_clicked_ok2(e):
        home1()
        txt_entry.visible = False
        Ok2.visible = False
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
        sys.exit("Error 404")

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
        Ok1.visible=False
        Ok2.visible = False
        txt_entry.visible=False
        txt_notentry.visible = False
        txt_registration.visible=False
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
        txt_nickname.value = ""
        txt_name.value = ""
        txt_second_name.value = ""
        txt_city.value = ""
        txt_age.value = ""
        txt_pasword.value = ""
        txt_check_nickname.value = ""
        txt_check_pasword.value = ""
        regist.visible = True
        login.visible = True
        close.visible = True
        hom.visible = False

    txt_nickname = ft.TextField(value="", hint_text="Enter nickname", width=300,)
    txt_name = ft.TextField(value="", hint_text="Enter your name", width=300)
    txt_second_name = ft.TextField(value="", hint_text="Enter your second name", width=300)
    txt_city = ft.TextField(value="", hint_text="Enter your city", width=300)
    txt_age = ft.TextField(value="", hint_text="Enter your age", width=300)
    txt_pasword = ft.TextField(value="", hint_text="Enter password", width=300)
    txt_check_nickname = ft.TextField(value="", hint_text="Enter nickname", width=300)
    txt_check_pasword = ft.TextField(value="", hint_text="Enter password", width=300)

    txt_registration=ft.Text(value="You have registered", size=30)
    txt_entry=ft.Text(value="You are logged", size=30)
    txt_notentry = ft.Text(value="You aren't logged", size=30)

    regist=ft.ElevatedButton(text="Registration",width=300, height= 40, on_click=button_clicked_start_registration)
    login=ft.ElevatedButton(text="Login",width=300, height= 40, on_click=button_clicked_start_entry)
    close=ft.ElevatedButton(text="Close",width=300, height= 40,color="white", bgcolor="red360" ,on_click=button_clicked_start_close)
    hom=ft.ElevatedButton(text="Back",width=300, on_click=home)
    enter1=ft.ElevatedButton(text="Enter",width=300, on_click=button_clicked_enter1)
    enter2=ft.ElevatedButton(text="Enter",width=300, on_click=button_clicked_enter2)
    Ok1 = ft.ElevatedButton(text="Ok", width=100, on_click=button_clicked_ok1)
    Ok2 = ft.ElevatedButton(text="Ok", width=100, on_click=button_clicked_ok2)

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
                enter2,
                txt_registration,
                txt_entry,
                txt_notentry,
                Ok1,
                Ok2
            ],

        )
    )
ft.app(target=main)

