country = input('where are you come from?')
age = input ('how old are you?')

if country == 'taiwan':
	if float(age) >= 18:
		print('you can drive!')
	else:
		print('you are too young to drive.')
elif country == 'america':
	if float(age) >= 16:
		print('you can drive!')
	else:
		print('you cannot drive!')

