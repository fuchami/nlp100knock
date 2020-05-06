# coding:utf-8
import pandas as pd

df = pd.read_csv('./popular-names.txt',sep='\t',header=None)

df[0].to_csv('./ch2/col1.txt',header=False,index=False)
df[1].to_csv('./ch2/col2.txt',header=False,index=False)