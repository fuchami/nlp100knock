# coding:utf-8

import pandas as pd
import sys

if len(sys.argv) == 1:
    print('set arg n')
else:
    n = int(sys.argv[1])
    df = pd.read_csv('./popular-names.txt', sep='\t', header=None)
    print(df.tail(n))

# tail -n 3 ./popular-names.txt