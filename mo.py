P = float(input('\nP')) / 100
N = int(input('N = ')) + 1

list_input = [int(i) for i in input(
    '\nEnter the values (separated by spaces):\n\n').split()]
list_input.sort()

result = P*N
rounded = round(result + .1)

if str(result)[-1] != '0':
    print(
        f'\nThe answer is in position {result} or {rounded}, which has a value of {list_input[rounded-1]}.\n')
else:
    print(
        f'\nThe answer is in position {rounded}, which has a value of {list_input[rounded-1]}.\n')

# print(f'\nThe value of position {rounded} is', list_input[rounded-1], '\n')
