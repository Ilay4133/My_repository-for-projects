
def registration_new_user(user_nickname, user_name, user_second_name, user_city, user_age, user_password):
    Users_DATA_File = open("Users_DATA_File.txt", "a+")
    Users_DATA_File.write(user_nickname)
    Users_DATA_File.write(user_name)
    Users_DATA_File.write(user_second_name)
    Users_DATA_File.write(user_city)
    Users_DATA_File.write(user_age)
    Users_DATA_File.write(user_password)
    Users_DATA_File.close()






def entry_user(check_user_nickname, chack_user_password):
    print(112)
