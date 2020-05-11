# coding:utf-8
from readMecab30 import readFile
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'

# 先にfilterで絞ってから辞書に入れる処理にしたほうがスマートでした
def countWord(block_list):
    wordCounts = {}
    for block in block_list:
        flg = list(filter(lambda x: x['surface'] == '猫', block))
        if len(flg) > 0:
            for b in block:
                if b['surface'] != '猫':
                    word = b['surface']
                    if word in wordCounts:
                        wordCounts[word] += 1
                    else:
                        wordCounts[word] = 1
    
    return wordCounts

block_list = readFile()
wordCounts = countWord(block_list)
wordCounts = sorted(wordCounts.items(), key=lambda x: x[1], reverse=True)[:10]

labels = [w[0] for w in wordCounts]
values = [w[1] for w in wordCounts]
target = list(zip(*wordCounts))

print(target)
plt.barh(*target)
plt.show()