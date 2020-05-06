# coding:utf-8

import pandas as pd
import json

df = pd.read_json('./ch3/jawiki-country.json', lines=True)

uk_df = df.query('title == "イギリス" ')
print(type(uk_df['text'].values))
print (uk_df['text'].values[0])
