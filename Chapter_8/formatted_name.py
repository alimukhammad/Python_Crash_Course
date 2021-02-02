

def get_formatted_name(first_name, last_name, middle_name=" "):
    #return full name neatly format
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name("jimi", "jo", "hendrix")
print(musician)

musician = get_formatted_name("jimi", "jo")
print(musician)