import re

f = open('/Users/lucienzak/Projet/runtrack-python/jour03/job01/domains.xml', 'r')
text = f.read().splitlines()
f.close()

count = 0
lineNumber = 0

for line in text:
    lineNumber += 1
    if re.search(r'\.[a-zA-Z]{2,8}', line):
        count += 1
        print('Trouvé à la ligne', lineNumber ,' : ',re.findall(r'\.[a-zA-Z]{2,6}', line)[-1], 'dans la ligne :',line)

print ('Nombre de récurences : ',count)
