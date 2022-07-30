# using dictionaries to store bdays in python. Written with vim

birthdays = {'Alice': 'apr 1', 'Bob': 'march 1', 'Carol': 'may 1'}

while True:
    print(birthdays)
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updates.')

