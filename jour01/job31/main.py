import itertools

word = input("Entrez un mot : ")
list = itertools.permutations(word)
newList = []

for i in list:
    newList.append(''.join(i))
newList.sort()

index = newList.index(word)

nextWord = newList[index + 1]

if nextWord == word:
    print('Le mot',word,'est le dernier mot possible')
else:
    print('Le mot suivant est :',nextWord)