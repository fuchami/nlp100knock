# coding:utf-8

import pandas as pd

df = pd.read_csv('./popular-names.txt',sep='\t',header=None)

print(len(df))

# wc -l popular-names.txt
# -> 2780 popular-names.txt