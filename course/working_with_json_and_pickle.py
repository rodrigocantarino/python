"""

Working with JSON and Pickle

"""

import json
import jsonpickle

ret = json.dumps(['product',{'PS4': ('2TB', 'New', '220V', 2340)}])
print(type(ret))
print(ret)

print('--------------------------------------------------------')
print('--------------------------------------------------------')


class Cat:

    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed

    @property
    def name(self):
        return self.__name

    @property
    def breed(self):
        return self.__breed


felix = Cat('Felix the Cat', 'Tuxedo cat')

print(felix.__dict__)

json_cat = json.dumps(felix.__dict__)

print(json_cat)

print('--------------------------------------------------------')
print('--------------------------------------------------------')

json_pickle_ret = jsonpickle.encode(felix)

print(json_pickle_ret)

print('--------------------------------------------------------')
print('--------------------------------------------------------')

# Writing json/pickle file
with open('jsonpickle.json', 'w') as file:
    file.write(json_pickle_ret)

print('--------------------------------------------------------')
print('--------------------------------------------------------')

# Reading json/pickle file
with open('jsonpickle.json', 'r') as file:
    file_content = file.read()
    r = jsonpickle.decode(file_content)
    print(r)
    print(type(r))

    print(r.name)
    print(r.breed)
