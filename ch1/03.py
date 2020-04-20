# coding:utf-8
import re
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

s = s.replace(',','').replace('.', '')

out = [len(w) for w in s.split(' ')]

# イケてない
# for i in s.split(' '):
#     out.append(len(i))
print(out)