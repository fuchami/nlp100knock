# coding:utf-8

"""
スマートに記述できる
https://qiita.com/kazmaw/items/4df328cba6429ec210fb
def n_gram(target, n):
    # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
    return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]
"""

def n_gram(raw, N=2):
    ngram = []
    for i in range(len(raw)):
        if len(raw[i:]) < N :
            return ngram
        ngram.append(raw[i:i+N])

s1 = "paraparaparadise"
s2 = "paragraph"

x = n_gram(s1)
y = n_gram(s2)
print(x)
print(y)

print(f'和集合: {set(x)|set(y)}')
print(f'積集合: {set(x)&set(y)}')
print(f'差集合: {set(x)-set(y)}')

print('se' in set(x)|set(y))