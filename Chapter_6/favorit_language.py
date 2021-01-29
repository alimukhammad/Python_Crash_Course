

favorit_languages = {
    'jet': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
friends = ['phil', 'sarah']
for name in favorit_languages.keys():
    print(name.title())

    if name in friends:
        print("   Hi   " + name.title() +
              ", I see your favorite language is " +
              favorit_languages[name].title() + "!")

# for name, language in favorit_languages.items():
#     print(name.title() + "'s favorit language is " + language.title() + ".")
#print("Sarah's favorit language is " + favorit_languages['sarah'].title())