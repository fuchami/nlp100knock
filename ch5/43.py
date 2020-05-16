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

class Chunk():
    def __init__(self, chunk_id, morphs, dst):
        self.chunk_id = chunk_id
        self.morphs = morphs
        self.dst = dst
        self.srcs = []
    
    def getMorphs(self):
        return self.morphs


def FetchMorp(block):
    block = block.split('\n')

    chunks = []
    morphs = []
    srcs_dict = {}

    for b in block:
        # new sentence!
        if b.startswith('*'):
            # morphs取れてたらchunk生成
            if len(morphs) > 0:
                chunks.append(Chunk(chunk_id, morphs, dst))
                # init
                morphs = []

            attr = b.split(' ')
            chunk_id = attr[1]
            dst = attr[2].replace('D', '')
            
            # srcs_dict[dst] = 係り元文節インデックスのリスト
            if dst in srcs_dict:
                srcs_dict[dst].append(chunk_id)
            else:
                srcs_dict[dst] = list(chunk_id)

        else:
            params = b.split('\t')
            if len(params) > 1:
                morphs.append(Morph(params))

    if len(morphs) > 0:
        chunks.append(Chunk(chunk_id, morphs, dst))

    # set srcs 
    for i, c in enumerate(chunks):
        if str(i) in srcs_dict:
            c.srcs = srcs_dict[str(i)]

    return chunks

def readCabocha():
    with open('./ch5/neko.txt.cabocha', mode='rt', encoding='utf-8') as f:
        block_list = f.read().split('EOS\n')

    block_list = list(filter(lambda x: x != '', block_list))
    block_list = [FetchMorp(block) for block in block_list]

    for b in block_list:
        for chunk in b:
            if int(chunk.dst) > -1:
                preText = ''.join([mo.surface if mo.pos != '記号' else '' for mo in chunk.morphs])
                prePos = [mo.pos for mo in chunk.morphs]
                postText = ''.join([mo.surface if mo.pos != '記号' else '' for mo in b[int(chunk.dst)].morphs])
                postPos = [mo.pos for mo in b[int(chunk.dst)].morphs]
                if '名詞' in prePos and '動詞' in postPos:
                    print(preText, postText, sep='\t')

if __name__ == "__main__":
    readCabocha()
