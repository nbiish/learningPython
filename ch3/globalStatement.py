# global statement in\out of functions in python. Written with vim

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
