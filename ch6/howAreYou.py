# sometimes you need to be asked..

print('How are you?')

feeling = input()

hopes = 'I hope things get better. Take a couple concious breaths.'

if 'not' in feeling.lower():
        print(hopes)
elif feeling.lower() == 'good' or 'great' or 'amazing':
	print('..cherish it..')
else:
	print(hopes)
