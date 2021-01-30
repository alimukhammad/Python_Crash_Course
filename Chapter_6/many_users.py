users = {
    'aeinstein': {
        'first':'alber',
        'last': 'einstein',
        'location': 'princton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    }
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['location']

    print("\tFull Name: " +full_name.title())
    print("\tLocation: " + location.title())
