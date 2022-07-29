# magic 8 ball v2 with list in python. Written with vim

import random

messages = ['It is certain', 
        'It is decidedly so', 
        'Yes definitely', 
        'Reply hazy try again', 
        'Ask again later', 
        'Concentrate and ask again', 
        'My reply is no', 
        'Outlook not so good', 
        'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])


