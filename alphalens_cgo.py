import pandas as pd
import numpy as np
import alphalens



factorcgo=pd.read_excel('factordata.xlsx')
#factorcgo=pd.DataFrame(factorcgo)
factorcgo=factorcgo.set_index(['tradedate','stockcode'])
factorcgo['cgofactor'] = pd.to_numeric(factorcgo['cgofactor'],errors='coerce')

price=pd.read_excel('pricedata.xlsx')
price=pd.DataFrame(price)
price=price.pivot(index='tradedate',columns='stockcode',values='closeprice')

price.index = pd.DatetimeIndex(price.index)
print(price)


ret=alphalens.utils.get_clean_factor_and_forward_returns(factorcgo,price,groupby=None,quantiles=5,bins=None,periods=(1,5,10),filter_zscore=20,groupby_labels=None)
print(ret)
#alphalens.tears.create_full_tear_sheet(ret,long_short=True,group_neutral=False)








 



