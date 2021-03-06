# coding:utf-8
from readMecab30 import readFile
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'

def countWord(block_list):
    wordCounts = {}
    for block in block_list:
        for b in block:
            word = b['base'] + "_" + b['pos'] + "_" + b['pos1']
            if word in wordCounts:
                wordCounts[word] += 1
            else:
                wordCounts[word] = 1
    return wordCounts

block_list = readFile()
wordCounts = countWord(block_list)
# valueで降順にソート
wordCounts = sorted(wordCounts.items(), key=lambda x: x[1], reverse=True)[:10]

labels = [w[0] for w in wordCounts]
values = [w[1] for w in wordCounts]
target = list(zip(*wordCounts))
print(target)
plt.barh(*target)
plt.show()