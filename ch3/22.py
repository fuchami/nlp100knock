# coding:utf-8
import pandas as pd

df = pd.read_json('./ch3/jawiki-country.json', lines=True)
uk_df_lines = df.query('title == "イギリス"')['text'].values[0].split('\n')

ans = list(filter(lambda x: "Category:" in x, uk_df_lines))
ans = [ a.replace("[[Category:", "").replace("]]", "").replace("|*", "") for a in ans]
print(ans[1:])