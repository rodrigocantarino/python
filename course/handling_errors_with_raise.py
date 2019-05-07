"""

Raise -> is a reserved key word and throw exceptions

How to use:

raise ErrorType(<ErrorMessage>)

OBS: if raise is executed it will stop the script execution

"""

# raise NameError('Called function/variable is not defined on this script')


def to_colour(text, colour):
    if type(text) is not str:
        raise TypeError('Text variable MUST BE a string')
    if type(colour) is not str:
        raise TypeError('Colour variable MUST BE a string')
    print(text + '\n' + colour)


# to_colour(2, [])

t = """
Mussum Ipsum, cacilds vidis litro abertis. Nullam volutpat risus nec leo commodo, ut interdum diam laoreet. 
Sed non consequat odio. Tá deprimidis, eu conheço uma cachacis que pode alegrar sua vidis. 
Delegadis gente finis, bibendum egestas augue arcu ut est. Suco de cevadiss deixa as pessoas mais interessantis.
"""

c = 'Black'

to_colour(t, c)

print('-------------------------------')

def to_colour(text, colour):
    colours = ('green', 'yellow', 'blue', 'white')

    if type(text) is not str:
        raise TypeError('Text variable MUST BE a string')
    if type(colour) is not str:
        raise TypeError('Colour variable MUST BE a string')
    if colour not in colours:
        raise ValueError(f'The colour MUST BE some of the colours {colours}!!!')

    print(text + '\n' + colour)


t = """
Mussum Ipsum, cacilds vidis litro abertis. Nullam volutpat risus nec leo commodo, ut interdum diam laoreet. 
Sed non consequat odio. Tá deprimidis, eu conheço uma cachacis que pode alegrar sua vidis. 
Delegadis gente finis, bibendum egestas augue arcu ut est. Suco de cevadiss deixa as pessoas mais interessantis.
"""

c = 'Black'

to_colour(t, c)
