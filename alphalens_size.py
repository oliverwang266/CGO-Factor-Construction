import pandas as pd
import numpy as np
import alphalens



factorsize=pd.read_csv('sizedata.csv')

factorsize=factorsize.set_index(['tradedate','stockcode'])
factorsize['size'] = pd.to_numeric(factorsize['size'],errors='coerce')

price=pd.read_csv('pricedata.csv')
price=pd.DataFrame(price)
price=price.pivot(index='tradedate',columns='stockcode',values='closeprice')



ret=alphalens.utils.get_clean_factor_and_forward_returns(factorsize,price,groupby=None,quantiles=5,bins=None,periods=(1,5,10),filter_zscore=20,groupby_labels=None)
alphalens.tears.create_full_tear_sheet(ret)
