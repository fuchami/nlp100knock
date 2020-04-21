# coding:utf-8
import random

def typo(t):
    if len(t) <= 4:
        return t
    else:
        tmp = list(t[1:-1])
        # 別回答
        # others = ramdom.sample(list(t[1:-1], len(word[1:-1])))
        random.shuffle(tmp)
        t = t[0] + ''.join(tmp) + t[-1]
        return t

raw = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
result =' '.join([typo(w) for w in raw.split()])
print(result)
