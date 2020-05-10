# coding:utf-8
"""
dump mecab file
$ mecab < ./ch4/neko.txt > ./ch4/neko.txt.mecab

表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
"""

def parseMeCab(block):
    res = []
    for line in block.split('\n'):
        if line == '':
            return res
        (surface, attr) = line.split('\t')
        attr = attr.split(',')
        lineDict = {
            'surface': surface,
            'base': attr[6],
            'pos': attr[0],
            'pos1': attr[1],
        }
        res.append(lineDict)

def readFile():
    with open('./ch4/neko.txt.mecab', mode='rt', encoding='utf-8') as f:
        block_list = f.read().split('EOS\n')
        block_list = list(filter(lambda x: x != '', block_list))
        block_list = [parseMeCab(block) for block in block_list]
    return block_list


if __name__ == "__main__":
    block_list = readFile()
    print(block_list[1])