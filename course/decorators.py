"""


Decorators


"""

# Decorator as function. Not recommended syntax.


def be_polite(func):
    def been():
        print('Nice to meet you!')
        func()
        print('Have a nice day!')
    return been


def greetings():
    print('Welcome here!')


# Test 1
test = be_polite(greetings)
test()

print('------------------------------------')

# Test 2


def hate():
    print('I HATE YOU!!!!')


polite_hate = be_polite(hate)
polite_hate()

print('------------------------------------')
print('------------------------------------')
print('------------------------------------')

# Decorator with syntax sugar. Recommended syntax.


def be_really_polite(func):
    def been_really():
        print('It is VERY nice to meet you!')
        func()
        print('Have a wonderful day!')
    return been_really


@be_really_polite  # Decorator sugar syntax. 
def introduce():
    print('My name is Rodrigo!!!')


introduce()
