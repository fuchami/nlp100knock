# coding:utf-8

""" block example
* 0 2D 0/1 -1.911675
名前    名詞,一般,*,*,*,*,名前,ナマエ,ナマエ
は      助詞,係助詞,*,*,*,*,は,ハ,ワ
* 1 2D 0/0 -1.911675
まだ    副詞,助詞類接続,*,*,*,*,まだ,マダ,マダ
* 2 -1D 0/0 0.000000
無い    形容詞,自立,*,*,形容詞・アウオ段,基本形,無い,ナイ,ナイ
。      記号,句点,*,*,*,*,。,。,。
"""

class Morph():
    def __init__(self, params):
        attr = params[1].split(',')

        self.surface = params[0]
        self.base    = attr[6]
        self.pos     = attr[0]
        self.pos1    = attr[1]
    
    def show(self):
        print(self.surface, self.base, self.pos, self.pos1)


def FetchMorp(block):
    res = []
    block = block.split('\n')
    for b in block:
        if not b.startswith('*'):
            params = b.split('\t')
            if len(params) > 1:
                res.append(Morph(params))
    
    return res


def readCabocha():
    with open('./ch5/neko.txt.cabocha', mode='rt', encoding='utf-8') as f:
        block_list = f.read().split('EOS\n')

    block_list = list(filter(lambda x: x != '', block_list))

    res = FetchMorp(block_list[2])
    for r in res:
        print(vars(r))

if __name__ == "__main__":
    readCabocha()
