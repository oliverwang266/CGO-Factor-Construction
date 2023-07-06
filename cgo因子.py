import pandas as pd
import numpy as np
import openpyxl as op
df = pd.read_excel('stockdata1.xlsx')
col1 = df['turnover']
col2 = df['1-turnover']
col3 = df['junjia']
CGO = pd.Series()

for i in range(len(col1)):
    print(i)
    if i < 60:
        CGO[i] = 0
        print('error')
    else:
        base = 1
        sum = 0
        weight = {}
        RP = 0
        for j in range(60):
            weightj = col1[i - 1 - j]
            if(j != 0):
                base = base * col2[i-j]
            weightj = weightj * base
            sum += weightj
            weight[59 - j] = weightj
        for j in range(60):
            if(sum==0):
                break
            weight[j] = weight[j] / sum
            RP += weight[j]*col3[i - 60 + j]
        if(RP==0):
            CGO[i] = 'error'
        if(RP!=0):
            CGO[i] = (col3[i] - RP) / RP

# 将 Series 对象转换成 DataFrame 对象，并将列命名为 'cgo'
df = df.join(pd.DataFrame({'CGO因子': CGO}))
df.to_excel('stockdata.xlsx', index = False, startcol = 8)

       
        
    














#df['result_turnoverweight'] = result
#df.to_excel('stockdata.xlsx', index=False)

