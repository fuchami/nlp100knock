# coding:utf-8

raw = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
txt = raw.replace('.', '')

ex_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
out_dict = {}

for i, word in enumerate(txt.split(),1):
    if i in ex_list:
        out_dict[word[:1]] = i
    else:
        out_dict[word[:2]] = i

print(out_dict)
