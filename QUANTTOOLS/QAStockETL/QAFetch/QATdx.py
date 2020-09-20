from QUANTAXIS import QA_fetch_get_future_day, QA_fetch_stock_min_adv
from QUANTTOOLS.QAStockETL.QAData.database_settings import tdx_dir
from QUANTAXIS.QAUtil import (QA_util_today_str, QA_util_get_pre_trade_date, QA_util_get_pre_trade_date,
                              QA_util_get_trade_range, QA_util_get_real_date,
                              QA_util_if_trade,QA_util_get_last_day,
                              QA_util_date_stamp)
import easyquotation
import pandas as pd
import akshare as ak

QA_fetch_get_usstock_day = QA_fetch_get_future_day

def QA_fetch_get_stock_realtime(code):
    quotation = easyquotation.use('sina')
    values = pd.DataFrame(quotation.stocks(code)).T
    values.index.name = 'code'
    return(values)

def QA_fetch_get_stock_real(code):
    quotation = easyquotation.use('sina')
    values = quotation.real(code)[code]
    return(values)

def QA_fetch_get_stock_close(code):
    return(float(QA_fetch_get_stock_realtime(code)['close']))

def QA_fetch_get_stock_realtm_ask(code):
    return(float(QA_fetch_get_stock_real(code)['sell']))

def QA_fetch_get_stock_realtm_askvol(code):
    return(float(QA_fetch_get_stock_real(code)['aks1_volume']))

def QA_fetch_get_stock_realtm_askvol5(code):
    res = float(QA_fetch_get_stock_realtime(code)[['aks1_volume','aks2_volume','aks3_volume','aks4_volume','aks5_volume']])
    return(float(res.aks1_volume + res.aks2_volume + res.aks3_volume + res.aks4_volume + res.aks5_volume))

def QA_fetch_get_stock_realtm_bid(code):
    return(float(QA_fetch_get_stock_real(code)['buy']))

def QA_fetch_get_stock_realtm_bidvol(code):
    return(float(QA_fetch_get_stock_real(code)['bid1_volume']))

def QA_fetch_get_stock_realtm_bidvol5(code):
    res = float(QA_fetch_get_stock_realtime(code)[['bid1_volume','bid2_volume','bid3_volume','bid4_volume','bid5_volume']])
    return(float(res.bid1_volume + res.bid2_volume + res.bid3_volume + res.bid4_volume + res.bid5_volume))

def QA_fetch_get_usstock_adj():
    pass

def QA_fetch_get_usstock_cik():
    pass

def QA_fetch_get_usstock_financial():
    pass

def QA_fetch_get_usstock_financial_calendar():
    pass

def QA_fetch_get_stock_industryinfo(file_name='tdxhy.cfg'):
    return(pd.read_csv(tdx_dir+file_name,
                       header=None,
                       sep='|',
                       dtype=str,
                       names=['market','code','TDXHY','SWHY','HHY'],
                       encoding='gb18030'))

def QA_fetch_get_index_info(file_name='tdxzs.cfg'):
    return(pd.read_csv(tdx_dir+file_name,
                       header=None,
                       sep='|',
                       dtype=str,
                       names=['index_name','code','cate','unknown1','unknown2','HY'],
                       encoding='gb18030'))

def QA_fetch_get_stock_delist():
    sh = ak.stock_info_sh_delist(indicator="终止上市公司")[['COMPANY_CODE','SECURITY_ABBR_A','LISTING_DATE','QIANYI_DATE']]
    sz = ak.stock_info_sz_delist(indicator="终止上市公司")
    sz.columns = ['code','name','LISTING_DATE','QIANYI_DATE']
    sh.columns = ['code','name','LISTING_DATE','QIANYI_DATE']
    sh = sh.assign(sse = 'sh')
    sz = sz.assign(sse = 'sz')
    sz = sz.append(sh)
    sz = sz.assign(QIANYI_DATE = sz.QIANYI_DATE.apply(lambda x:str(x)[0:10]))
    return(sz)

def QA_fetch_get_stock_half_realtime(code, source = 'sina'):
    quotation = easyquotation.use(source)
    res = pd.DataFrame(quotation.stocks(code) ).T[['date','open','high','low','now','turnover','volume','close']]
    res = res.reset_index().rename(columns={'index':'code',
                                            'close':'pctchange',
                                            'now':'close',
                                            'turnover':'volume',
                                            'volume':'amount'})
    res = res.assign(pctchange=res.close/res.pctchange-1).set_index(['date','code'])
    return(res.astype('float64'))

def half_ohlc(data):
    data = data.reset_index().set_index('datetime')
    res = data.resample('12H').agg({'open': 'first', 'high': 'max',  'low': 'min', 'close': 'last','volume': 'sum','amount': 'sum'})
    return(res)

def QA_fetch_get_stock_half(code, start, end):
    if QA_util_if_trade(start):
        start_date = QA_util_get_last_day(start)
    else:
        start_date = QA_util_get_real_date(start)

    if QA_util_if_trade(end):
        end = QA_util_get_last_day(end)
    else:
        end = QA_util_get_real_date(end)

    price = QA_fetch_stock_min_adv(code, start_date, end, frequence='60min').data
    price = price.groupby('code').apply(half_ohlc).reset_index().set_index('datetime')
    price = price.assign(pctchange = price.close/price.close.shift()-1)
    price = price.between_time("00:00", "09:00").reset_index().rename(columns={'datetime':'date'}).dropna()
    price['date_stamp'] = price['date'].apply(lambda x: QA_util_date_stamp(str(x)[0:10]))
    return(price)