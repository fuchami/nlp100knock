# coding:utf-8
import pandas as pd
import re
import requests

def getUrl(dc):
    url_file = dc['国旗画像'].replace(' ', '_')
    url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + url_file + '&prop=imageinfo&iiprop=url&format=json'
    data = requests.get(url)
    print(data.text)
    return re.search(r'"url":"(.+?)"', data.text).group(1)

""" 全部入り"""
def removeMk(v):
    r1 = re.compile("'+")
    r2 = re.compile('\[\[(.+\||)(.+?)\]\]')
    r3 = re.compile('\{\{(.+\||)(.+?)\}\}')
    r4 = re.compile('<\s*?/*?\s*?br\s*?/*?\s*>')
    v = r1.sub('', v)
    v = r2.sub(r'\2', v)
    v = r3.sub(r'\2', v)
    v = r4.sub('', v)
    return v

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

r = re.compile('\[\[(.+\||)(.+?)\]\]')
info_dict = {k: removeMk(v) for k, v in info_dict.items()}
print(remove_innner_line(remove_stress(info_dict)))

""" get 国旗画像 """
print(getUrl(info_dict))