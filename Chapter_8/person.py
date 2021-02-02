

def build_person(first_name, last_name, age=''):
    #info about person
    person = {'first': first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jack', 'hendrix', age=30)
print(musician)