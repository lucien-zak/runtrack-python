import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import re

f = open('jour03/job13/data.txt', 'r')
list = []
for line in f:
    for letter in line:
        if letter.isalpha() and re.search(r'[a-zA-Z]', letter):
            list.append(letter.capitalize())
i = 0
newList = {}
while i < len(list) - 1:
    if list[i] in newList:
        newList[list[i]].append(list[i + 1])
    else:
        newList[list[i]] = [list[i + 1]]
    i += 1


    
# plt.plot(['A', 'A'],["B", 'C'], color='blue', marker='o')
# plt.show()

