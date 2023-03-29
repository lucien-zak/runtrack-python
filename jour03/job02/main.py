import re
nbChar = input('Entrez le nombre de caractères : ')
f = open('/Users/lucienzak/Projet/runtrack-python/jour03/job01-2/data.txt', 'r')
count = 0
lines = 0
for line in f:
    lines += 1
    for word in line.split():
        if re.search(r'\w+', word):
            if len(word) == int(nbChar):
                count += 1

print('Nombre de mots avec',nbChar,'caractères :',count)
