"""
Maps -> In Python is also known as Dictionaries

They are represented by braces {}
"""

incoming = {
    'jan': 6000,
    'feb': 6200,
    'mar': 5900
}

print(incoming)

print('------------- Iterate on a Dictionary -------------')
for key in incoming:
    print(key)

print('')

for key in incoming:
    print(incoming[key])  # print value

print('')

for key in incoming:
    print(f'In {key.upper()} the incoming was US$ {incoming[key]}.')

print('')
print('------------- Get the Dictionary Keys -------------')
print(incoming.keys())
for key in incoming.keys():
    print(incoming[key])  # print value

print('')
print('------------- Get the Dictionary Values -------------')
print(incoming.values())

for value in incoming.values():
    print(value)  # print value

print('')
print('------------- Unpack Dictionary -------------')

print(incoming.items())

for key, value in incoming.items():
    print(f'Key = {key} & Value = {value}.')


print('------------- Using Methods: Sum, Max value, Min Value, Length of a Dictionary -------------')

# Methods: Sum, Max value, Min Value
# Works ONLY if all values are int or float
print(sum(incoming.values()))
print(max(incoming.values()))
print(min(incoming.values()))

# Method: Size (length)
# Works anytime
print(len(incoming.values()))
