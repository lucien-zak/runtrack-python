import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import re

f = open('jour03/job08/data.txt', 'r')
list = []
for line in f:
    for word in line.split():
        if word[0].isalpha() and re.search(r'[a-zA-Z]', word[0]):
                list.append(word[0].capitalize())          
        
list.sort()

plt.hist(list, density=True, bins=26, range=(0,26), color='blue', edgecolor='black', align='left')
plt.xlabel('Première lettre des mots')
plt.ylabel('Fréquence')
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.title('Histogramme de d\'apparation des premières lettres par mots')
plt.show()