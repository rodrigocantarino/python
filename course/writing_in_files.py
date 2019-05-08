"""

Writing in files

write() -> The passed parameter must be a String!

"""

# IF the file doesn't exists, the file will be automatically created.
# ATTENTION: IF the file DOES exists, ALL the file content will be overwritten!!!!
with open('mussum_ipsum2.txt', mode='w') as file:
    file.write('\n Mussum Ipsum is a very funny way to use a dummy text on programming. ')
    file.write('\n Mussum Ipsum is a very funny way to use a dummy text on programming SECOND LINE ADDED. ')
    file.write('\n Mussum Ipsum is a very funny way to use a dummy text on programming THIRD LINE ADDED. ')

with open('mussum_ipsum3.txt', mode='w') as file:
    file.write('\n Mussum Ipsum!!! \n' * 20)

with open('mussum_ipsum_test_input.txt', mode='w') as file:
    while True:
        input_txt = input('Type anything: ')
        if input_txt != 'end' and input_txt != 'out':
            file.write(f'{input_txt} \n')
        else:
            break

