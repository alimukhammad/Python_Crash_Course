

def greet_users(names):
    #print greeting
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'lee']
greet_users(usernames)