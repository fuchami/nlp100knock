# coding:utf-8

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
    
    def getSurfaces(self):
        return ''.join([m.surface for m in self.morphs])
    
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
    b = block_list[5]

    """ for debug """
    # print('--------------------------------------------------')
    # for r in b:
    #     print(vars(r))
    #     morphs = r.getMorphs()
    #     for m in morphs:
    #         print(vars(m))
    # print('--------------------------------------------------')

    for chunk in b:
        if '名詞' in [m.pos for m in chunk.morphs]:
            res = []
            res.append(chunk.getSurfaces())

            while chunk.dst != '-1':
                chunk = b[int(chunk.dst)]
                res.append(chunk.getSurfaces())
            
            print(' -> '.join(res))

if __name__ == "__main__":
    readCabocha()
