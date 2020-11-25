#find the largest number so far that will find from this code

largestNumber = -1
itrator=1

for theNumber in [14,51,32,87,190,255,145,22]:
    #check the numer is largestNumber or not
    if largestNumber<theNumber :
        largestNumber =theNumber
    print('largest number :',largestNumber,'and this number is :',theNumber,'on',itrator,'th iteration')
    itrator=itrator+1

print('-----------')
print('--=======--')
print('-----------')
