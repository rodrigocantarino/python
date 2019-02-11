"""

String type

On Python a data is considered String:
- Data between single quotation marks or triple: 'string', '''string'''
- Data between double quotes or triple double quotes: "string", \"""string\"""

Scape char: \
 - Example: 'I don\'t Know!'

"""

single_quotation_marks = 'string'
triple_single_quotation_marks = '''string'''

double_quotes = 'string'
triple_double_quotes = """string"""

triple_double_quotes_multiple_lines = """Mussum Ipsum, cacilds vidis litro abertis. \n
Diuretics paradis num copo é motivis de denguis. Não sou faixa preta cumpadi, sou preto inteiris, inteiris. 
In elementis mé pra quem é amistosis quis leo. Todo mundo vê os porris que eu tomo, 
mas ninguém vê os tombis que eu levo!"""

scape_char = 'I don\'t Know strings in Python!';

print(single_quotation_marks, triple_single_quotation_marks, double_quotes, triple_double_quotes)
print(type(single_quotation_marks), type(triple_single_quotation_marks), type(double_quotes), type(triple_double_quotes))

print(triple_double_quotes_multiple_lines)

print(scape_char)

# To upper
print(scape_char.upper())

# To lower
print(scape_char.lower())

# To title
print(scape_char.title())

""" 
Split - Return a list of the words in the string, using sep as the delimiter string. 
The delimiter according which to split the string. 
None (the default value) means split according to any whitespace,
and discard empty strings from the result.
"""
print(triple_double_quotes_multiple_lines.split())

# Getting part of the string (substring) string[start_position, length]
# scape_char -> I do
print(scape_char[0:4])

# Print string backwards
print(single_quotation_marks[::-1])
print(triple_double_quotes_multiple_lines[::-1])

# Replace
print(scape_char.replace("don't", "do"))

# Fun fact
bird = "arara"
print(bird)
print(bird[::-1])
