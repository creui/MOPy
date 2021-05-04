P = float(input('\nP')) / 100
N = int(input('N = ')) + 1

result = P*N
rounded = round(result + .1)

if str(result)[-1] == '5':
	print(f'\n{result} or {rounded}. The answer is in position {rounded}.')
else:
	print(f'\n{int(result)}. The answer is in position {rounded}.')

print('\n(Make sure to arrange the values first before finding the answer.)\n')