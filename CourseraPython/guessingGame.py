import random


#generate a random number between 1 and 100

randnum = random.randint(1,101)

count =0
guess=-99

while(guess!=randnum):
    #Get the user's guess
    guess = (int)(input('Enter your guess between 1 and 100: '))
    if guess < randnum:
        print('higher')
    elif guess > randnum:
        print('lower')
    else :
        print('you guess it!')
        break
    count=count+1
#end of while loop

print('You took '+ str(count)+' steps to guess the number')
