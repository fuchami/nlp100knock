# coding:utf-8
from readMecab30 import readFile
import matplotlib.pyplot as plt
import math

plt.rcParams['font.family'] = 'AppleGothic'

def countWord(block_list):
    wordCounts = {}
    for block in block_list:
        for b in block:
            word = b['surface']
            if word in wordCounts:
                wordCounts[word] += 1
            else:
                wordCounts[word] = 1
    return wordCounts

block_list = readFile()
wordCounts = countWord(block_list)

# 38.Histogram
ans = wordCounts.values()
plt.hist(ans, range=(1,20))
plt.show()

# 39. Zipfの法則 両対数グラフ
ans = sorted(wordCounts.items(), key=lambda x: x[1], reverse=True)
ranks = [math.log(r+1) for r in range(len(ans))]
values = [math.log(a[1]) for a in ans]

plt.figure(figsize=(8,8))
plt.scatter(ranks, values)
plt.show()