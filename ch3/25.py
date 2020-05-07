# coding:utf-8
import sys
import pandas as pd
import re

df = pd.read_json('./ch3/jawiki-country.json', lines=True)
uk_df = df.query('title == "イギリス"')['text'].values[0]
uk_df_lines = uk_df.split('\n')

read_flg = False
info_dict = {}

""" 気合の実装 頭が悪そう """
for line in uk_df_lines:
    if read_flg: 
        if line.startswith('|'):
            row = line.split('=', 1)
            print(row)
            key = row[0].replace('|','').rstrip()
            value = row[1].lstrip()
            info_dict[key] = value

    if read_flg and line.startswith("}}"): break
    if line.startswith("{{基礎情報"):
        read_flg = True

print(info_dict)

""" u++ result 
ls, fg = [], False
template = '基礎情報'
p1 = re.compile('\{\{' + template)
p2 = re.compile('\}\}')
p3 = re.compile('\|')
p4 = re.compile('<ref(\s|>).+?(</ref>|$)')
for l in uk_df_lines:
    if fg:
        ml = [p2.match(l), p3.match(l)]
        if ml[0]:
            break
        if ml[1]:
            ls.append(p4.sub('', l.strip()))
    if p1.match(l):
        fg = True
p = re.compile('\|(.+?)\s=\s(.+)')
ans = {m.group(1): m.group(2) for m in [p.match(c) for c in ls]}
print(ans)
"""