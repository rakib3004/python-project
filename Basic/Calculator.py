print('Welcome to the Calculator Program')
option = input('Would you like to add, subtract, multiply or divide?')
num1 = int(input('Please enter the first number:'))
num2 = int(input('Please enter the second number:'))


if(option=='add'):
    result=num1+num2
    sign='+'

elif(option=='subtract'):
    result = num1 - num2
    sign = '-'

elif(option=='multiply'):
    result = num1 - num2
    sign = '*'

elif(option=='divide'):
    result =num1 / num2
    sign = '/'


print(num1,sign,num2,'=',result)
