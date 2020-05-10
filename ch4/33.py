# coding:utf-8
from readMecab30 import readFile

block_list = readFile()

def extract(block):
    res = []
    for i in range (1, len(block)-1 ):
        if block[i-1]['pos'] == '名詞' and block[i]['base'] == 'の' and block[i+1]['pos'] =='名詞':
            res.append(block[i-1]['surface']+block[i]['surface']+block[i+1]['surface'])
    
    return res

extract_list = [extract(block) for block in block_list]
# 空のリストを除去
extract_list = list(filter(lambda x: len(x) >= 1, extract_list))
print(extract_list)