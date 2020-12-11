iFile = open("Vocabulary_list","r")

iWordList = iFile.readlines()
#print(iWordList)

iWordSet = set(iWordList)

jFile = open("Vocabulary_set","w")
jFile.writelines(iWordSet)