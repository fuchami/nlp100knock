# coding:utf-8
from readMecab30 import readFile

def extract(block):
    res = []
    tmp = []

    for b in block:
        if b['pos'] == '名詞':
            tmp.append(b['surface'])
        elif len(tmp) > 1:
            res.append(''.join(tmp))
            tmp = []
        else:
            tmp = []
    return res

block_list = readFile()
extract_list = [extract(block) for block in block_list]
extract_list = list(filter(lambda x: len(x) > 0, extract_list))

print(extract_list[:30])
