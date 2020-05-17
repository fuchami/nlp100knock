# coding:utf-8
import pydot
# わかんなかったのでu++氏のコードを拝借

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
    
    def show(self):
        print(f'chunk_id:{self.chunk_id}, dst:{self.dst}, srcs:{self.srcs}')
        for m in self.morphs:
            print(vars(m))

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

    print('--------------------------------------------------')
    b = block_list[5]
    for r in b:
        print(vars(r))
        morphs = r.getMorphs()
        for m in morphs:
            print(vars(m))
    print('--------------------------------------------------')

    with open('./ch5/47.txt', 'w') as f:
        for b in block_list:
            for i, m in enumerate(b):
                if 'サ変接続' in [s.pos1 for s in m.morphs] and 'を' in [s.surface for s in m.morphs] and i + 1 < len(b) and b[i + 1].morphs[0].pos == '動詞':
                    text = ''.join([s.surface for s in m.morphs]) + b[i + 1].morphs[0].base
                    if len(m.srcs) > 0:
                        preMorphs = [b[int(s)].morphs for s in m.srcs]
                        preMorphsFiltered = [list(filter(lambda x: '助詞' in x.pos, pm)) for pm in preMorphs]
                        preSurface = [[p.surface for p in pm] for pm in preMorphsFiltered]
                        preSurface = list(filter(lambda x: x != [], preSurface))
                        preSurface = [p[0] for p in preSurface]
                        preText = list(filter(lambda x: '助詞' in [p.pos for p in x], preMorphs))
                        preText = [''.join([p.surface for p in pt]) for pt in preText]
                        if len(preSurface) > 0:
                            f.writelines('\t'.join([text, ' '.join(preSurface), ' '.join(preText)]))
                            f.write('\n')

if __name__ == "__main__":
    readCabocha()
