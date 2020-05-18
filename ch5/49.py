# coding:utf-8
""" u++氏の実装を参考に '"""

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
    
    def getSurfaces(self, replace_word='X'):
        return ''.join([replace_word if m.pos == '名詞' else m.surface for m in self.morphs])
    
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

def noun_noun_path(s):
    pl, nl = [], [c for c in s if '名詞' in [m.pos for m in c.morphs]]
    for i in range(len(nl) - 1):
        st1 = [''.join([m.surface if m.pos != '名詞' else 'X' for m in nl[i].morphs])]
        for e in nl[i + 1:]:
            dst, p = nl[i].dst, []
            st2 = [''.join([m.surface if m.pos != '名詞' else 'Y' for m in e.morphs])]
            while int(dst) != -1 and dst != s.index(e):
                p.append(s[int(dst)])
                dst = s[int(dst)].dst
            if len(p) < 1 or p[-1].dst != -1:
                mid = [''.join([m.surface for m in c.morphs if m.pos != '記号']) for c in p]
                pl.append(st1 + mid + ['Y'])
            else:
                mid, dst = [], e.dst
                while not s[int(dst)] in p:
                    mid.append(''.join([m.surface for m in s[int(dst)].morphs if m.pos != '記号']))
                    dst = s[int(dst)].dst
                ed = [''.join([m.surface for m in s[int(dst)].morphs if m.pos != '記号'])]
                pl.append([st1, st2 + mid, ed])
    return pl

def readCabocha():
    with open('./ch5/neko.txt.cabocha', mode='rt', encoding='utf-8') as f:
        block_list = f.read().split('EOS\n')

    block_list = list(filter(lambda x: x != '', block_list))
    block_list = [FetchMorp(block) for block in block_list]

    for b in block_list:
        pl = (noun_noun_path(b))
        for p in pl:
            if isinstance(p[0], str):
                print(' -> '.join(p))
            else:
                print(p[0][0], ' -> '.join(p[1]), p[2][0], sep=' | ')

if __name__ == "__main__":
    readCabocha()
