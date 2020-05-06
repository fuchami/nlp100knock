# coding:utf-8
import pandas as pd

def show(df, N=5):
    print(df.head(N))

df = pd.read_csv('./popular-names.txt', sep='\t', header=None)
show(df)
