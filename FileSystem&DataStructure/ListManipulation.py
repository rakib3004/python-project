from math import sqrt


def findPrime(x):
    aX=34
    i=2
    for i in range(sqrt(x)):
        if(x%i == 0): return False

    return True


primeNumbers=[]
iRange =2020
#while i<=iRange :
 #   if(findPrime(i)==True):
  #      primeNumbers.append(i)

print(primeNumbers)

