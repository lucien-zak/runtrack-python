import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import re

f = open('jour03/job05/data.txt', 'r')
list = []
for line in f:
    for word in line.split():
        list.append(len(word))
list.sort()

plt.hist(list, density=True, bins=26, range=(0,26), color='blue', edgecolor='black')
plt.xlabel('Nombre de caractères')
plt.ylabel('Fréquence')
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.title('Histogramme de longueur des mots')
plt.show()