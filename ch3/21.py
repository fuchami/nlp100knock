# coding:utf-8
import pandas as pd

df = pd.read_json('./ch3/jawiki-country.json', lines=True)
uk_df = df.query('title == "イギリス"')['text'].values[0]

uk_df_lines = uk_df.split('\n')

ans = list(filter(lambda x: 'Category:' in x , uk_df_lines))
for a in ans:
    print(a)