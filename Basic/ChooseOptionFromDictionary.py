cricket =dir()
cricket["Test"] = "This is a 5 day cricket match"
cricket["ODI"] = "This is a 50 overs cricket match"
cricket["T20"]= "This is a 20 overs cricket match"
cricket["Batsman"] = "Who hits the ball"
cricket["Bowler"] = "Who throw ball against batsman"
cricket["Fielder"] = "Who catch and get the ball from the field"
cricket["Keeper"] = "Who stands behind the wicket and catch the ball"
cricket["Umpire"] = "Who determine and get decision of all actions in a match"

print("What do you want to know:")
getQ = input("1.Test\n2.ODI\n3.T20\n4.Batsman\n5.Bowler\n6.Fielder\n7.Keeper\n8.Umpire\nExit by :quit")
print(cricket[getQ])
while getQ!="quit":
    getQ=input()
    print(cricket[getQ])