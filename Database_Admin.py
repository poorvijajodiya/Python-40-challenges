print("Welcome to the Database Admin Program")
log_on_information = {
    "admin00" : 'heyimthere',
    "monika" : 'dogismypet',
    "john" : 'ratismypet',
    "george" : 'dontbeworry',
    "rohan" : 'tadadataada',
}
user = input("Enter your username: ").lower()
if user in log_on_information:
    pswd = input("Enter your password: ")
    if pswd == log_on_information[user]:
        print("Hello {}! You are logged in!".format(user))
        if user == 'admin00':
            for k,v in log_on_information.items():
                print("Username:{}\t\tpassword:{}".format(k,v))
        else:
            inp = input("Would you like to change your password: ")
            if inp.startswith('y'):
                i = input("What would you like your new password to be: ")
                if len(i) >= 8:
                    log_on_information[user] = i
                else:
                    print("{} not the minimum eight characters".format(i))
                print("{} your password is {}".format(user,log_on_information[user] ))
            else:
                print("Thank you Goodbye!!!!!")
    else:
        print("Incorrect password!!!")
else:
    print("Username not in database, goodbye.")