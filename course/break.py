"""

Using break to exit loop structures


"""

string = 'Rodrigo'

for c in string:
    print(c)
    if c == 'd':
        break


while True:
    condition = input('Type "stop" to exit the execution: ')
    if condition == 'stop':
        break
