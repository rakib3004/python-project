import random

def get_def_and_pop(word_list,word_dictonary):
    random_index = random.randrange(len(word_list))
    word = word_list.pop(random_index)
    defination = word_dictonary.get(word)
    return  word,defination


def get_word_definition(rawString):
    tWord, tDefination = rawString.split(',', 1)
    return  tWord,tDefination

iFile = open("Vocabulary_list", "r")

iWordList = iFile.readlines()
# print(iWordList)

iWordSet = set(iWordList)

#jFile = open("Vocabulary_set", "w")
#jFile.writelines(iWordSet)

iDictionaries = dict()
for iString in iWordSet:
    word, defination = get_word_definition(iString)
    iDictionaries[word]=defination


while True :
    iList = list(iDictionaries)
    choiceList = []
    for xTerm in range(4):
        word,defination = get_def_and_pop(iList,iDictionaries)
        choiceList.append(defination)
        random.shuffle(choiceList)

    print(word)
    print('---Choose--the--right--answer---')
    for inx,choice in enumerate(choiceList):
        print(inx+1,choice)
    choice = int(input('Enter 1,2,3 or 4 : 0 to exit\n'))
    if choiceList[choice-1] == defination:
         print("Correct\n")
    elif choice==0:
         exit(0)
    else:
        print("Incorrect")