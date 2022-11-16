loopNumber = input()
loopNumber = int(loopNumber)

for i in range(loopNumber):
    stringnumber = input()
    list= stringnumber.replace(" ","")
    result="1/"+str(len(list))
    print(result)



