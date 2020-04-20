# coding:utf-8

def n_gram(raw, N=2):
    ngram = []
    for i in range(len(raw)):
        if len(raw[i:]) < N :
            return ngram
        ngram.append(raw[i:i+N])

# 単語bi-gram
raw = "I am an NLPer".split()
print(n_gram(raw))

# 文字bi-gram
raw = ("I am an NLPer".replace(' ', ''))
print(n_gram(raw))
