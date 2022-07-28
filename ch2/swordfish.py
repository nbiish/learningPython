# continue statements in python written with vim

while True:
    print('Who are you?')
    name = input()
    if name != 'Nbiish':
        continue
    print('Aanii/Hello Nbiish. What\'s your pass? (it is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
