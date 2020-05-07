# coding:utf-8
import sys
import pandas as pd
import re

def remove_stress(dc):
    r = re.compile("'+")
    return {k: r.sub('',v) for k, v in dc.items()}

def remove_innner_line(dc):
    r = re.compile('\[\[(.+\||)(.+?)\]\]')
    return {k: r.sub('',v) for k, v in dc.items()}

df = pd.read_json('./ch3/jawiki-country.json', lines=True)
uk_df = df.query('title == "イギリス"')['text'].values[0]
uk_df_lines = uk_df.split('\n')

read_flg = False
info_dict = {}

p4 = re.compile('<ref(\s|>).+?(</ref>|$)')

for line in uk_df_lines:
    if read_flg: 
        if line.startswith('|'):
            row = line.split('=', 1)
            key = row[0].replace('|','').rstrip()
            value = p4.sub('', row[1].strip())

            info_dict[key] = value

    if read_flg and line.startswith("}}"): break
    if line.startswith("{{基礎情報"):
        read_flg = True

print(remove_innner_line(remove_stress(info_dict)))