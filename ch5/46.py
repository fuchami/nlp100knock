# coding:utf-8
import pydot

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

    for block in block_list[5:6]:
        for chunk in block:
            if len(chunk.srcs) > 0:
                # 述語
                predicate = [mo.base if mo.pos == '動詞' else '' for mo in chunk.morphs]
                predicate = list(filter(lambda x: x !='', predicate))

                # 助詞
                particlesMorphs = [block[int(s)].morphs for s in chunk.srcs]
                particles = [list(filter(lambda x: '助詞' in x.pos, pm)) for pm in particlesMorphs]
                particles = [[p.surface for p in pm] for pm in particles]
                particles = list(filter(lambda x: x != [], particles))
                particles = [ p[0] for p in particles]

                # 格フレーム
                kaku = [[p.surface for p in pm] for pm in particlesMorphs]
                kaku = ' '.join([ ''.join(k) for k in kaku])

                if len(predicate) > 0:
                    print(predicate[0], ' '.join(particles), kaku ,sep='\t')

if __name__ == "__main__":
    readCabocha()
