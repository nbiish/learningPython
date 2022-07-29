# usderstaning global variables within functions in python. Written with vim

def spam():
    global eggs
    eggs = 'spam'   # This is a GLOBAL VARIABLE

def bacon():
    eggs = 'bacon'  # This is a LOCAL VARIABLE

def ham():
    print(eggs)     # This is a GLOBAL VARIABLE


eggs = 42           # This is a GLOBAL VARIABLE
spam()
print(eggs)
