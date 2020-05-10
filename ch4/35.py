# coding:utf-8
from readMecab30 import readFile

"""
defaultdict使うとkeyの確認がいらないらしい
https://upura.hatenablog.com/entry/2020/04/20/121729
"""

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
wordCounts = sorted(wordCounts.items(), key=lambda x: x[1], reverse=True)

print(wordCounts[:10])