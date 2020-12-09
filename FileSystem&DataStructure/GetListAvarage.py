numberList = list()
while True :
    intA = input("Enter Number")
    if intA==0 : break
    else :  numberList.append(intA)

print(sum(numberList)/len(numberList))