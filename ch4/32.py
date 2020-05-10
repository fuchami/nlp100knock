# coding:utf-8

from readMecab30 import readFile

block_list = readFile()

def extract(block):
    res = list(filter(lambda x: x['pos'] == '動詞', block))
    res = [ r['base'] for r in res]
    return res

block_list = [extract(block) for block in block_list]
print(block_list[3])
