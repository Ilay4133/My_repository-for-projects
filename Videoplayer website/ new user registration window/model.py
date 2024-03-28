i=0
def registration_new_user(user_nickname, user_name, user_second_name, user_city, user_age, user_password):
    for i in range (100):
        if i == 0:
            Users_DATA_File = open("Users_DATA_File.txt", "w+")
            Users_DATA_File.write(i,"user_nickname:", user_nickname)
            Users_DATA_File.write(i,"user_name:", user_name)
            Users_DATA_File.write(i,"user_second_name:", user_second_name)
            Users_DATA_File.write(i,"user_city:", user_city)
            Users_DATA_File.write(i,"user_age:", user_age)
            Users_DATA_File.write(i,"user_password:", user_password)
            Users_DATA_File.close()
            i=i+1
            break
        else:
            Users_DATA_File = open("Users_DATA_File.txt", "a+")
            Users_DATA_File.write(i,"user_nickname:", user_nickname)
            Users_DATA_File.write(i,"user_name:", user_name)
            Users_DATA_File.write(i,"user_second_name:", user_second_name)
            Users_DATA_File.write(i,"user_city:", user_city)
            Users_DATA_File.write(i,"user_age:", user_age)
            Users_DATA_File.write(i,"user_password:", user_password)
            Users_DATA_File.close()
            i=i+1
            break
def entry_user(check_user_nickname, chack_user_password):
    print(112)
