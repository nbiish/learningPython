# using in and not in with python lists. Written in vim

myPets = ['Zo', 'Po', 'Fo']
print('Enter a pet name: ')
name = input()
if name not in myPets:
    print('I don\'t have a pet named ' + name)
else:
    print(name + ' is my pet.')


