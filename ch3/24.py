# coding:utf-8
import pandas as pd
import re

df = pd.read_json('./ch3/jawiki-country.json', lines=True)
uk_df = df.query('title == "イギリス"')['text'].values[0]

for result in re.findall(r'\[\[(ファイル|File):([^]|]+?)(\|.*?)+\]\]', uk_df):
    print(result)