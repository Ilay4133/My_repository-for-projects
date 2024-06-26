import flet as ft
import sys
import sqlite3


open('Users_DATA_File.txt', 'a').close()

def main(page):
    page.scroll = "always"
    page.title="AnimeGo"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.theme_mode="dark"

    class User:
        def registration_new_user(self):
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

        def registration_new_user1(self):
            db = sqlite3.connect('Users_Data_File.Data')
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS users (
                nickname TEXT PRIMARY KEY,
                name TEXT,
                second_name TEXT,
                city TEXT,
                age INTEGER,
                password INTEGER
            )""")
            cur.execute(f"INSERT INTO users VALUES('{geting_user_nickname}', '{geting_user_name}', '{geting_user_second_name}', '{geting_user_city}', '{geting_user_age}', '{int(geting_user_password)}')")
            db.commit()
            db.close()

        def entry_user1(self):
            admin="Ilay"
            admin_pasword="1111"
            db = sqlite3.connect('Users_Data_File.Data')
            cur = db.cursor()
            cur.execute(f"SELECT * FROM users WHERE nickname ='{geting_check_user_nickname}' AND password = '{geting_check_user_password}'")
            if cur.fetchone() != None:
                if geting_check_user_nickname == admin and geting_check_user_password == admin_pasword:
                    return 3
                else:
                    return 2
            else:
                return 0

            db.commit()
            db.close()


        def entry_user(self):
            global i
            i = 2
            with open("Users_DATA_File.txt") as f:
                lines = f.readlines()

            for line in lines:
                if geting_check_user_nickname == line[:-1]:
                    for line in lines:
                        if geting_check_user_password == line[:-1]:
                            return 2
                        else:
                            i = 1
                else:
                    if i == 1:
                        pass
                    else:
                        i = 0
            if i == 0:
                return 0
            if i == 1:
                return 1

        def get_entry_user(self):
            if tom.entry_user1() == 2:
                txt_entry.visible = True
                Ok3.visible = True
            elif tom.entry_user1() == 1:
                txt_not_entry1.visible = True
            elif tom.entry_user1() == 0:
                txt_not_entry2.visible = True
                Ok2.visible = True
            elif tom.entry_user1() == 3:
                txt_entry3.visible = True
                Ok4.visible = True

        def get_user_nickname(self):
            global geting_user_nickname
            geting_user_nickname = txt_nickname.value
            return geting_user_nickname

        def get_user_name(self):
            global geting_user_name
            geting_user_name = txt_name.value
            return geting_user_name

        def get_user_second_name(self):
            global geting_user_second_name
            geting_user_second_name = txt_second_name.value
            return geting_user_second_name

        def get_user_city(self):
            global geting_user_city
            geting_user_city = txt_city.value
            return geting_user_city

        def get_user_age(self):
            global geting_user_age
            geting_user_age = txt_age.value
            return geting_user_age

        def get_user_password(self):
            global geting_user_password
            geting_user_password = txt_pasword.value
            return geting_user_password

        def get_check_user_nickname(self):
            global geting_check_user_nickname
            geting_check_user_nickname = txt_check_nickname.value
            return geting_check_user_nickname

        def get_chack_user_password(self):
            global geting_check_user_password
            geting_check_user_password = txt_check_pasword.value
            return geting_check_user_password

    tom=User()


# ========================================================================


    class Page:
        def del2(self):
            txt_filters.visible=False
            txt_entry3.visible = False
            regist.visible=False
            login.visible=False
            close.visible=False
            txt_nickname.visible=False
            txt_name.visible=False
            txt_second_name.visible=False
            txt_city.visible=False
            txt_age.visible=False
            txt_pasword.visible=False
            txt_check_nickname.visible=False
            txt_check_pasword.visible=False
            hom.visible=False
            enter1.visible=False
            enter2.visible=False
            txt_registration.visible=False
            txt_entry.visible=False
            txt_not_entry1.visible=False
            txt_not_entry2.visible=False
            Ok1.visible=False
            Ok2.visible=False
            Ok3.visible = False
            Ok4.visible = False

        def button_clicked_enter1(self,e):
            tom.get_user_nickname()
            tom.get_user_name()
            tom.get_user_second_name()
            tom.get_user_city()
            tom.get_user_age()
            tom.get_user_password()
            tom.registration_new_user1()
            txt_nickname.value = ""
            txt_name.value = ""
            txt_second_name.value = ""
            txt_city.value = ""
            txt_age.value = ""
            page1.del1()
            txt_registration.visible = True
            Ok1.visible = True
            page.update()

        def button_clicked_enter2(self, e):
            tom.get_check_user_nickname()
            tom.get_chack_user_password()
            tom.entry_user1()
            page1.del1()
            tom.get_entry_user()

            if tom.entry_user1 == 2:
                Ok3.visible = True
            elif tom.entry_user1 == 3:
                Ok4.visible = True
            elif tom.entry_user1 == 0:
                Ok2.visible = True
            page.update()

        def button_clicked_ok1(self, e):
            page1.home1()
            txt_registration.visible = False
            Ok1.visible = False
            page.update()

        def button_clicked_ok2(self, e):
            page1.home1()
            txt_entry.visible = False
            Ok2.visible = False
            page.update()

        def button_clicked_start_registration(self, e):
            page1.undel1()
            regist.visible = False
            login.visible = False
            close.visible = False
            page.update()

        def button_clicked_start_entry(self,e):
            regist.visible = False
            login.visible = False
            close.visible = False
            page1.undel2()
            page.update()

        def button_clicked_start_close(self,e):
            regist.visible = False
            login.visible = False
            close.visible = False
            page.update()
            sys.exit("Error 404")

        def home(self, e):
            page1.home1()
            page1.del1()
            page.update()

        def del1(self):
            txt_filters1.visible = False
            txt_filters2.visible = False
            txt_filters3.visible = False
            txt_filters4.visible = False
            txt_filters5.visible = False
            txt_filters6.visible = False
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
            Ok1.visible = False
            Ok2.visible = False
            Ok3.visible = False
            Ok4.visible = False
            txt_entry.visible = False
            txt_not_entry1.visible = False
            txt_not_entry2.visible = False
            txt_entry3.visible = False
            txt_registration.visible = False

        def reg_home(self, e):
            glavpage1.del3()
            page1.home1()
            page.update()


        def undel1(self):
            txt_nickname.visible = True
            txt_name.visible = True
            txt_second_name.visible = True
            txt_city.visible = True
            txt_age.visible = True
            txt_pasword.visible = True
            hom.visible = True
            enter1.visible = True

        def undel2(self):
            txt_check_nickname.visible = True
            txt_check_pasword.visible = True
            hom.visible = True
            enter2.visible = True

        def home1(self):
            txt_nickname.value = ""
            txt_name.value = ""
            txt_second_name.value = ""
            txt_city.value = ""
            txt_age.value = ""
            txt_pasword.value = ""
            txt_check_nickname.value = ""
            txt_check_pasword.value = ""
            page1.del1()
            regist.visible = True
            login.visible = True
            close.visible = True
            hom.visible = False


#========================================================================


    class Glavpage():
        def del4(self):
            poisk.value = ""
            txt_filters.visible = False
            txt_filters1.visible = False
            txt_filters2.visible = False
            txt_filters3.visible = False
            txt_filters4.visible = False
            txt_filters5.visible = False
            txt_filters6.visible = False
            txt_add_anime.visible = True

            page.update()


        def click_add_anime(self,e):
            glavpage1.del4()
            print(1)



        def add_glavpage(self):
            return ft.Row([icon_home, icon_adminhome, poisk, icon_poisk, exit_acaunt, admin_set, icon_to_add_anime],[page.horizontal_alignment],
                   [page.vertical_alignment])
            page.update()

        def add_filters(self):
            return ft.Column([txt_filters, txt_filters1, txt_filters2, txt_filters3, txt_filters4, txt_filters5, txt_filters6],[page.vertical_alignment], [page.horizontal_alignment])
            page.update()

        def glavhome(self,e):
            page.vertical_alignment = ft.MainAxisAlignment.START
            page.horizontal_alignment = ft.CrossAxisAlignment.START
            glavpage1.del3()
            txt_filters.visible = True
            txt_filters1.visible = True
            txt_filters2.visible = True
            txt_filters3.visible = True
            txt_filters4.visible = True
            txt_filters5.visible = True
            txt_filters6.visible = True
            icon_home.visible = True
            poisk.visible = True
            icon_poisk.visible = True
            exit_acaunt.visible = True
            page1.del2()
            page.update()

        def del3(self):
            poisk.value=""
            txt_filters.visible=False
            icon_adminhome.visible=False
            icon_home.visible = False
            poisk.visible=False
            icon_poisk.visible=False
            exit_acaunt.visible=False
            admin_set.visible=False
            icon_to_add_anime.visible=False
            page.update()

    class Admin_Glavpage(Glavpage):

        def glavhome(self,e):
            page.vertical_alignment = ft.MainAxisAlignment.START
            page.horizontal_alignment = ft.CrossAxisAlignment.START
            glavpage1.del3()
            txt_filters.visible = True
            txt_filters1.visible = True
            txt_filters2.visible = True
            txt_filters3.visible = True
            txt_filters4.visible = True
            txt_filters5.visible = True
            txt_filters6.visible = True
            icon_adminhome.visible = True
            poisk.visible = True
            icon_poisk.visible = True
            exit_acaunt.visible = True
            admin_set.visible = True
            icon_to_add_anime.visible = True
            page1.del2()
            page.update()


# ========================================================================


    glavpage1=Glavpage()
    glavpage_admin1 = Admin_Glavpage()
    page1=Page()

#TextField
    txt_nickname = ft.TextField(value="", hint_text="Enter nickname", width=300,)
    txt_name = ft.TextField(value="", hint_text="Enter your name", width=300)
    txt_second_name = ft.TextField(value="", hint_text="Enter your second name", width=300)
    txt_city = ft.TextField(value="", hint_text="Enter your city", width=300)
    txt_age = ft.TextField(value="", hint_text="Enter your age", width=300)
    txt_pasword = ft.TextField(value="", hint_text="Enter password", width=300)
    txt_check_nickname = ft.TextField(value="", hint_text="Enter nickname", width=300)
    txt_check_pasword = ft.TextField(value="", hint_text="Enter password", width=300)

#ElevatedButton glavpage
    txt_filters=ft.Text(value="Filters", width=200)
    txt_filters1 = ft.ElevatedButton(text="Filters1", width=200)
    txt_filters2 = ft.ElevatedButton(text="Filters2", width=200)
    txt_filters3 = ft.ElevatedButton(text="Filters3", width=200)
    txt_filters4 = ft.ElevatedButton(text="Filters4", width=200)
    txt_filters5 = ft.ElevatedButton(text="Filters5", width=200)
    txt_filters6 = ft.ElevatedButton(text="Filters6", width=200)

#pisk TextField
    poisk=ft.TextField(value="", hint_text="What are you looking for anime?", width=1000)

#icons
    icon_adminhome=ft.IconButton(ft.icons.ADOBE_SHARP,icon_size=60,icon_color="red500",on_click=glavpage_admin1.glavhome)
    icon_home = ft.IconButton(ft.icons.ADOBE_SHARP, icon_size=60, icon_color="red500",on_click=glavpage1.glavhome)
    icon_poisk=ft.IconButton(ft.icons.LOUPE_SHARP,icon_size=60,icon_color="white")
    exit_acaunt=ft.IconButton(ft.icons.EXIT_TO_APP_SHARP,icon_size=60,icon_color="green400", on_click=page1.reg_home)
    admin_set = ft.IconButton(ft.icons.ADMIN_PANEL_SETTINGS, icon_size=60, icon_color="blue400")
    icon_to_add_anime = ft.IconButton(ft.icons.PLUS_ONE, icon_size=60, icon_color="blue400", on_click=glavpage1.click_add_anime)

#text
    txt_add_anime = ft.Text(value="Add anime", size=30)

    txt_registration=ft.Text(value="You have registered", size=30)
    txt_entry3 = ft.Text(value="You are logged (admin status)", size=30)
    txt_entry=ft.Text(value="You are logged", size=30)
    txt_not_entry1 = ft.Text(value="You aren't logged, uncorrect password", size=30)
    txt_not_entry2 = ft.Text(value="You aren't registration", size=30)

#ElevatedButton registration
    regist=ft.ElevatedButton(text="Registration",width=300, height= 40, on_click=page1.button_clicked_start_registration)
    login=ft.ElevatedButton(text="Login",width=300, height= 40, on_click=page1.button_clicked_start_entry)
    close=ft.ElevatedButton(text="Close",width=300, height= 40,color="white", bgcolor="red360" ,on_click=page1.button_clicked_start_close)
    hom=ft.ElevatedButton(text="Back",width=300, on_click=page1.home)
    enter1=ft.ElevatedButton(text="Enter",width=300, on_click=page1.button_clicked_enter1)
    enter2=ft.ElevatedButton(text="Enter",width=300, on_click=page1.button_clicked_enter2)
    Ok1 = ft.ElevatedButton(text="Ok", width=100, on_click=page1.button_clicked_ok1)
    Ok2 = ft.ElevatedButton(text="Ok2", width=100, on_click=page1.button_clicked_ok2)
    Ok3 = ft.ElevatedButton(text="Ok3", width=100, on_click=glavpage1.glavhome)
    Ok4 = ft.ElevatedButton(text="Ok4", width=100, on_click=glavpage_admin1.glavhome)

    page1.del1()

    page.add(glavpage1.add_glavpage())
    page.add(glavpage1.add_filters())

    Glavpage.del3(1)

    page.add(
        ft.Column(
            [
                txt_add_anime,
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
                txt_entry3,
                txt_entry,
                txt_not_entry1,
                txt_not_entry2,
                Ok1,
                Ok2,
                Ok3,
                Ok4,
            ],

        )
    )
ft.app(target=main)