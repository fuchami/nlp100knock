# coding:utf-8
"""

小文字アルファベットは97-122
http://www3.nit.ac.jp/~tamura/ex2/ascii.html

chr:アスキーコード→文字
ord:文字→アスキーコード

"""

def cipher(raw):
    result = ""
    for w in raw:
        if ord(w) > 96 and ord(w) < 123:
            result += chr(219 -ord(w))
        else:
            return raw
    return result

# u++ result
def cipher_(raw):
    txt = [chr(219 - ord(w)) if 97 <= ord(w) <=122 else w for w in raw]
    return ''.join(txt)

    

txt = 'fuchami'
print(cipher(txt))

txt = 'ufxsznr'
print(cipher(txt))

print(cipher_(txt))

