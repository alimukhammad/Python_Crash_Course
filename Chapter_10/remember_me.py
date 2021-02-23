import json

def get_stored_user():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)

def greet_user():
        username = get_stored_user()#input("What is your name? ")
        if username:
            print("Welcome back, " + username)
        else:
            username = get_new_username()
            filename = 'username.json'
            with open(filename, 'w') as f_obj:
                json.dump(username, f_obj)
                print("We'll remember you when you come back, " + username)
greet_user()
    #     with open(filename, 'w') as f_obj:
    #         json.dump(username, f_obj)
    #         print("We'll remember you when you come back, " + username)
    # else:
    #     print("Welcome back, " + username)


#
# username = input("What is your name? ")
#
# filename = 'username.json'
# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print("We'll remember you when You come back, " + username)