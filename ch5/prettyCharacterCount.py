# using "pretty print" with dictionaries in python. Written in vim

import pprint

message = 'It was a bright cold day in April, and the clocks were striing thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(pprint.pformat(count))
