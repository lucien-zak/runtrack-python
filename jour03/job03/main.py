import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import re

f = open('jour03/job03/data.txt', 'r')
list = []
for line in f:
    for word in line.split():
        for letter in word:
            if letter.isalpha() and re.search(r'[a-zA-Z]', letter):
                list.append(letter.capitalize())
list.sort()

plt.hist(list, density=True, bins=26, range=(0,26), color='blue', edgecolor='black', align='left')
plt.xlabel('Lettres')
plt.ylabel('Fréquence')
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.title('Histogramme d\'apparition des lettres')
plt.show()