# coding:utf-8

import pandas as pd

df = pd.read_csv('./popular-names.txt',sep='\t',header=None)

df.to_csv('./ch2/01ans.txt', header=False, index=False, sep=' ')