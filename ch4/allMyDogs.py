# printing from list in python. Written with vim

dogNames = []
while True:
    print('Enter name of dog ' + str(len(dogNames) + 1) +
            ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    dogNames = dogNames + [name]
print('The dog names are: ')
for name in dogNames:
    print(' ' + name)
