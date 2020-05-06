# coding:utf-8
import pandas as pd

df1 = pd.read_csv('./ch2/col1.txt',sep='\t',header=None)
df2 = pd.read_csv('./ch2/col2.txt',sep='\t',header=None)

df = pd.concat([df1, df2], axis=1)
df.to_csv('./ch2/ans03.txt', sep='\t', header=False,index=False)