def fizzbuzz(rang):
	
	# Counter
	i = 1
	three_multies = 0
	five_multies = 0
	both_multies = 0
	fizzbuzz_values = []

	# loop
	while i <= rang:
		state = ''

		# 3 multiples
		if i % 3 == 0:
			state += 'Fizz '
			three_multies += 1

		# 5 multiples
		if i % 5 == 0:
			state += 'Buzz'
			five_multies += 1

		# both multiples
		if i % 3 == 0 and i % 5 == 0:
			both_multies += 1
			fizzbuzz_values.append(i)

		# incrimaentor
		i += 1

		# empty state catcher
		if state == '':
			continue

		# Fizz/buzz Displayer
		print(state) 

	# Results
	print(f'Total 3 multiples: {three_multies}')
	print(f'Total 5 multiples: {five_multies}')
	print(f'Total both multiples: {both_multies}')
	print(f'Fizzbuzz Values: {fizzbuzz_values}')

fizzbuzz(10000000)