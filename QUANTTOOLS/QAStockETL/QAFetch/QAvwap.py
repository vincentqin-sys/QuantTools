from QUANTTOOLS.QAStockETL.QAFetch.QAUsFinancial import QA_fetch_get_usstock_day_xq, QA_fetch_get_stock_min_sina
from QUANTAXIS.QAUtil import QA_util_date_stamp,QA_util_get_pre_trade_date,QA_util_log_info,QA_util_get_trade_range
from QUANTAXIS.QAFetch.QAQuery_Advance import QA_fetch_stock_min_adv
from scipy import stats
import pandas as pd
import math
from QUANTAXIS.QAIndicator.base import CROSS

def rolling_ols(y):
    '''
    滚动回归，返回滚动回归后的回归系数
    rb: 因变量序列
    '''
    #y = pd.DataFrame.ewm(y,alpha=1.0/24,ignore_na=True).mean().values
    model = stats.linregress(y=y, x=pd.Series(range(1,len(y)+1)))
    return(math.atan(model.slope)*180/math.pi)

def spc(data, N= 5):
    data[['vamp_c']]= data.rolling(window=N).agg({'vamp':rolling_ols})
    return(data)

def QA_fetch_get_stock_vwap(code, start_date, end_date, period = '1', type = 'crawl'):
    QA_util_log_info("JOB Get {} Minly data for {code} ======= from {start_date} to {end_date}".format(period, code=code, start_date=start_date,end_date=end_date))

    if type == 'crawl':
        data = QA_fetch_stock_min_adv(code,start_date, end_date,frequence='1min').data
    elif type == 'real':
        data = QA_fetch_get_stock_min_sina(code, period=period, type='qfq').reset_index(drop=True).set_index(['datetime','code']).drop(columns=['date_stamp'])

    try:
        data = data.assign(date=data.reset_index().datetime.apply(lambda x:str(x)[0:10]).tolist(),
                           HM=data.reset_index().datetime.dt.strftime('%H:%M').values,
                           amt=((data['high'] +data['low']) / 2) * data['volume'])
        data = data.assign(camt = data.groupby(['date','code'])['amt'].cumsum(),
                           cvolume = data.groupby(['date','code'])['volume'].cumsum(),
                           close_p = data.groupby(['date','code'])['close'].shift(),
                           high_p = data.groupby(['date','code'])['high'].shift(),
                           low_p = data.groupby(['date','code'])['low'].shift(),
                           close_p2 = data.groupby(['date','code'])['close'].shift(2),
                           high_p2 = data.groupby(['date','code'])['high'].shift(2),
                           low_p2 = data.groupby(['date','code'])['low'].shift(2))
        data[['AMT_P','VOL_P']] = data.groupby(['HM','code'])[['camt','cvolume']].shift()
        data['AMT_UP'] = data['camt'] / data['AMT_P'] - 1
        data['vamp'] = data['camt'] / data['cvolume']
        data['VAMP_JC'] = CROSS(data['close'], data['vamp'])
        data['VAMP_SC'] = CROSS(data['vamp'], data['close'])
        data['vamp_c'] = data.groupby(['date','code']).apply(lambda x:spc(x))['vamp_c']
    except:
        QA_util_log_info("JOB No {} Minly data for {code} ======= from {start_date} to {end_date}".format(period, code=code, start_date=start_date,end_date=end_date))
        data = None

    return(data)
