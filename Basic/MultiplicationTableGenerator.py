print('Multiplication table generator')
print('******************************')
number = int(input('Enter a number:'))
print(number, 'Multiplication Table')

for i in range(11):
    if(i==0): continue
    print(i, 'X', number, '=', i*number)