# coding:utf-8
import pandas as pd
import re

df = pd.read_json('./ch3/jawiki-country.json', lines=True)

uk_df = df.query('title == "イギリス"')['text'].values[0]
uk_df_lines = uk_df.split('\n')

ans = list(filter(lambda x: x.startswith('='), uk_df_lines))

for a in ans:
    count = (a.count('=') // 2) -1
    name = a.replace('=', '').replace(' ', '')
    print(f'{name} :{count}')


# u++ result
for section in re.findall(r'(=+)([^=]+)\1\n', uk_df):
    print(f'{section[1].strip()}\t{len(section[0]) - 1}')