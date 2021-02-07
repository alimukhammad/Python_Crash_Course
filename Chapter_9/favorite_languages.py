

from collections import OrderedDict

favorit_languages = OrderedDict()

favorit_languages['jen'] = 'python'
favorit_languages['sarah'] = 'c'
favorit_languages['edward'] = 'ruby'
favorit_languages['phil'] = 'python'

for name, language in favorit_languages.items():
    print(name.title() + "'s favorit language is " +
          language.title())