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

print(iDictionaries)
