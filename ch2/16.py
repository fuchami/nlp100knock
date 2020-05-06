# coding:utf-8
import pandas as pd
import sys



if len(sys.argv) == 1:
    print('set arg n')
else:
    n = int(sys.argv[1])
    df = pd.read_csv('./popular-names.txt', sep='\t', header=None)

    row_num = len(df) // n
    print(f'row_num: {row_num}')

    for i in range(n+1):
        df.iloc[i * row_num:(i+1) *row_num].to_csv(f'./ch2/popular-names_{i}.txt', sep='\t', header=False, index=False)


# $ split -l 3 ./popular-names.txt ./ch2/ans16