
import numpy
import pandas as pd
import datetime
import math
import QUANTAXIS as QA
from QUANTAXIS.QAUtil import (DATABASE, QA_util_date_stamp,
                              QA_util_date_valid, QA_util_log_info, QA_util_code_tolist, QA_util_date_str2int, QA_util_date_int2str,
                              QA_util_to_json_from_pandas, QA_util_today_str,QA_util_get_pre_trade_date,QA_util_datetime_to_strdate,
                              QA_util_add_months,QA_util_getBetweenQuarter)
from QUANTAXIS.QAFetch.QAQuery_Advance import QA_fetch_future_list_adv
from QUANTAXIS.QAFetch.QAQuery import QA_fetch_stock_basic_info_tushare
from QUANTTOOLS.QAStockETL.FuncTools.financial_mean import financial_dict, dict2
from QUANTTOOLS.QAStockETL.FuncTools.base_func import pct,index_pct,time_this_function

def QA_fetch_stock_industry(stock_code):
    '''
    根据tushare 的数据库查找上市的日期
    :param stock_code: '600001'
    :return: string 上市日期 eg： '2018-05-15'
    '''
    items = QA_fetch_stock_basic_info_tushare()
    for row in items:
        if row['code'] == stock_code:
            return row['industry']

def QA_fetch_financial_report(code, start_date, end_date, type ='report', ltype='EN', db=DATABASE):
    """获取专业财务报表

    Arguments:
        code {[type]} -- [description]
        report_date {[type]} -- [description]

    Keyword Arguments:
        ltype {str} -- [description] (default: {'EN'})
        db {[type]} -- [description] (default: {DATABASE})

    Raises:
        e -- [description]

    Returns:
        pd.DataFrame -- [description]
    """

    if code is None:
        code = list(QA_fetch_future_list_adv()['code'])

    if isinstance(code, str):
        code = [code]

    if start_date is None:
        start = '1995-01-01'
    else:
        start = start_date

    if end_date is None:
        end = QA_util_today_str()
    else:
        end = end_date

    collection = db.financial
    num_columns = [item[:3] for item in list(financial_dict.keys())]
    CH_columns = [item[3:] for item in list(financial_dict.keys())]
    EN_columns = list(financial_dict.values())

    try:
        if type == 'report':
            cursor = collection.find({
                'code': {'$in': code}, "report_date": {
                    "$lte": QA_util_date_stamp(end),
                    "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
            data = pd.DataFrame([item for item in cursor])
        elif type == 'crawl':
            cursor = collection.find({
                'code': {'$in': code}, "crawl_date": {
                    "$lte": QA_util_date_stamp(end),
                    "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
            data = pd.DataFrame([item for item in cursor])
        else:
            print("type must be one of [report, crawl]")

        if len(data) > 0:
            res_pd = pd.DataFrame(data)
            if ltype in ['CH', 'CN']:

                cndict = dict(zip(num_columns, CH_columns))
                cndict['283']='283'
                try:
                    cndict['284'] = '284'
                    cndict['285'] = '285'
                    cndict['286'] = '286'
                except:
                    pass
                cndict['_id']='_id'
                cndict['code']='code'
                cndict['report_date']='report_date'
                cndict['crawl_date']='crawl_date'
                res_pd.columns = res_pd.columns.map(lambda x: cndict[x])
            elif ltype is 'EN':
                endict=dict(zip(num_columns,EN_columns))
                endict['283']='283'
                try:
                    endict['284'] = '284'
                    endict['285'] = '285'
                    endict['286'] = '286'
                except:
                    pass
                endict['_id']='_id'
                endict['code']='code'
                endict['report_date']='report_date'
                endict['crawl_date']='crawl_date'
                res_pd.columns = res_pd.columns.map(lambda x: endict[x])

            res_pd['crawl_date'] = res_pd['crawl_date'].apply(lambda x: datetime.datetime.fromtimestamp(math.floor(x)))
            res_pd['report_date'] = res_pd['report_date'].apply(lambda x: datetime.datetime.fromtimestamp(math.floor(x)))
            return res_pd.replace(-4.039810335e+34, numpy.nan).set_index(['report_date', 'code'], drop=False)
        else:
            return None
    except Exception as e:
        raise e

def QA_fetch_stock_financial_calendar(code, start, end=None, format='pd',type = 'day', collections=DATABASE.report_calendar):
    '获取股票日线'
    #code= [code] if isinstance(code,str) else code
    # code checking
    code = QA_util_code_tolist(code)

    if start is None:
        start = '1995-01-01'
    else:
        start = start

    if end is None:
        end = QA_util_today_str()
    else:
        end = end

    if QA_util_date_valid(end):

        __data = []
        if type == 'report':
            cursor = collections.find({
                'code': {'$in': code}, "report_date": {
                    "$lte": QA_util_date_stamp(end),
                    "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
            res = pd.DataFrame([item for item in cursor])
        elif type == 'day':
            cursor = collections.find({
                'code': {'$in': code}, "real_date": {
                    "$lte": QA_util_date_stamp(end),
                    "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
            res = pd.DataFrame([item for item in cursor])
        elif type == 'crawl':
            cursor = collections.find({
                'code': {'$in': code}, "crawl_date": {
                    "$lte": QA_util_date_stamp(end),
                    "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
            res = pd.DataFrame([item for item in cursor])
        else:
            print("type must be one of [report, day, crawl]")


        try:
            res = res.drop_duplicates(
                (['report_date', 'code']))
            res = res.ix[:, ['code', 'name', 'pre_date', 'first_date', 'second_date',
                             'third_date', 'real_date', 'codes', 'report_date', 'crawl_date']]
            res['real_date'] = res['real_date'].apply(lambda x: datetime.datetime.fromtimestamp(math.floor(x)))
            res['crawl_date'] = res['crawl_date'].apply(lambda x: datetime.datetime.fromtimestamp(math.floor(x)))
            res['report_date'] = res['report_date'].apply(lambda x: datetime.datetime.fromtimestamp(math.floor(x)))
        except:
            res = None
        if format in ['P', 'p', 'pandas', 'pd']:
            return res
        elif format in ['json', 'dict']:
            return QA_util_to_json_from_pandas(res)
        # 多种数据格式
        elif format in ['n', 'N', 'numpy']:
            return numpy.asarray(res)
        elif format in ['list', 'l', 'L']:
            return numpy.asarray(res).tolist()
        else:
            print("QA Error QA_fetch_stock_financial_calendar format parameter %s is none of  \"P, p, pandas, pd , json, dict , n, N, numpy, list, l, L, !\" " % format)
            return None
    else:
        QA_util_log_info(
            'QA Error QA_fetch_stock_financial_calendar data parameter start=%s end=%s is not right' % (start, end))


def QA_fetch_stock_divyield(code, start, end=None, format='pd',type = 'day', collections=DATABASE.stock_divyield):
    '获取股票日线'
    #code= [code] if isinstance(code,str) else code
    # code checking
    code = QA_util_code_tolist(code)

    if QA_util_date_valid(end):

        __data = []
        if type == 'report':
            cursor = collections.find({
                'a_stockcode': {'$in': code}, "report_date": {
                    "$lte": QA_util_date_stamp(end),
                    "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
            res = pd.DataFrame([item for item in cursor])
        elif type == 'day':
            cursor = collections.find({
                'a_stockcode': {'$in': code}, "reg_date": {
                    "$lte": QA_util_date_stamp(end),
                    "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
            res = pd.DataFrame([item for item in cursor])
        elif type == 'crawl':
            cursor = collections.find({
                'a_stockcode': {'$in': code}, "crawl_date": {
                    "$lte": QA_util_date_stamp(end),
                    "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
            res = pd.DataFrame([item for item in cursor])
        else:
            print("type must be one of [report, day, crawl]")
        #res=[QA_util_dict_remove_key(data, '_id') for data in cursor]

        try:
            res = res.drop_duplicates(
                (['dir_dcl_date', 'a_stockcode']))
            res = res.ix[:, ['a_stockcode', 'a_stocksname', 'div_info', 'div_type_code', 'bonus_shr',
                             'cash_bt', 'cap_shr', 'epsp', 'ps_cr', 'ps_up', 'reg_date', 'dir_dcl_date',
                             'a_stockcode1', 'ex_divi_date', 'prg', 'report_date', 'crawl_date']]
            res['reg_date'] = res['reg_date'].apply(lambda x: datetime.datetime.fromtimestamp(math.floor(x)))
            res['crawl_date'] = res['crawl_date'].apply(lambda x: datetime.datetime.fromtimestamp(math.floor(x)))
            res['report_date'] = res['report_date'].apply(lambda x: datetime.datetime.fromtimestamp(math.floor(x)))
        except:
            res = None
        if format in ['P', 'p', 'pandas', 'pd']:
            return res
        elif format in ['json', 'dict']:
            return QA_util_to_json_from_pandas(res)
        # 多种数据格式
        elif format in ['n', 'N', 'numpy']:
            return numpy.asarray(res)
        elif format in ['list', 'l', 'L']:
            return numpy.asarray(res).tolist()
        else:
            print("QA Error QA_fetch_stock_divyield format parameter %s is none of  \"P, p, pandas, pd , json, dict , n, N, numpy, list, l, L, !\" " % format)
            return None
    else:
        QA_util_log_info(
            'QA Error QA_fetch_stock_divyield data parameter start=%s end=%s is not right' % (start, end))

def QA_fetch_financial_TTM(code, start, end = None, format='pd', collections=DATABASE.financial_TTM):
    '获取财报TTM数据'
    #code= [code] if isinstance(code,str) else code
    # code checking
    code = QA_util_code_tolist(code)

    if QA_util_date_valid(end):
        __data = []

        cursor = collections.find({
            'CODE': {'$in': code}, "date": {
                "$lte": QA_util_date_stamp(end),
                "$gte": QA_util_date_stamp(start)}}, batch_size=10000)
        #res=[QA_util_dict_remove_key(data, '_id') for data in cursor]

        res = pd.DataFrame([item for item in cursor])
        try:
            res = res.drop('_id', axis=1).drop_duplicates((['REPORT_DATE', 'CODE']))
        except:
            res = None
        if format in ['P', 'p', 'pandas', 'pd']:
            return res
        elif format in ['json', 'dict']:
            return QA_util_to_json_from_pandas(res)
        # 多种数据格式
        elif format in ['n', 'N', 'numpy']:
            return numpy.asarray(res)
        elif format in ['list', 'l', 'L']:
            return numpy.asarray(res).tolist()
        else:
            print("QA Error QA_fetch_financial_TTM format parameter %s is none of  \"P, p, pandas, pd , json, dict , n, N, numpy, list, l, L, !\" " % format)
            return None
    else:
        QA_util_log_info(
            'QA Error QA_fetch_financial_TTM data parameter start=%s end=%s is not right' % (start, end))

def QA_fetch_stock_fianacial(code, start, end = None, format='pd', collections=DATABASE.stock_financial_analysis):
    '获取quant基础数据'
    #code= [code] if isinstance(code,str) else code
    # code checking
    code = QA_util_code_tolist(code)
    if QA_util_date_valid(end):
        cursor = collections.find({
            'CODE': {'$in': code}, "date_stamp": {
                "$lte": QA_util_date_stamp(end),
                "$gte": QA_util_date_stamp(start)}}, batch_size=10000)
        #res=[QA_util_dict_remove_key(data, '_id') for data in cursor]
        res = pd.DataFrame([item for item in cursor])
        try:
            res.columns = [i.lower() if i == 'CODE' else i for i in list(res.columns)]
            res = res.drop(['date_stamp','_id'], axis=1).drop_duplicates((['code', 'date']))
            res['RNG_RES'] = res['AVG60_RNG'] *60 / res['RNG_60']
        except:
            res = None
        if format in ['P', 'p', 'pandas', 'pd']:
            #res['report_date'] = pd.to_datetime(res['report_date']/1000, unit='s')
            return res
        elif format in ['json', 'dict']:
            return QA_util_to_json_from_pandas(res)
        # 多种数据格式
        elif format in ['n', 'N', 'numpy']:
            return numpy.asarray(res)
        elif format in ['list', 'l', 'L']:
            return numpy.asarray(res).tolist()
        else:
            print("QA Error QA_fetch_financial_TTM format parameter %s is none of  \"P, p, pandas, pd , json, dict , n, N, numpy, list, l, L, !\" " % format)
            return None
    else:
        QA_util_log_info(
            'QA Error QA_fetch_financial_TTM data parameter start=%s end=%s is not right' % (start, end))

def QA_fetch_stock_alpha(code, start, end=None, format='pd', collections=DATABASE.stock_alpha):
    '获取股票日线'
    #code= [code] if isinstance(code,str) else code
    # code checking
    code = QA_util_code_tolist(code)

    if QA_util_date_valid(end):

        __data = []
        cursor = collections.find({
            'code': {'$in': code}, "date_stamp": {
                "$lte": QA_util_date_stamp(end),
                "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
        #res=[QA_util_dict_remove_key(data, '_id') for data in cursor]

        res = pd.DataFrame([item for item in cursor])
        try:
            res = res.drop_duplicates(
                (['code', 'date'])).set_index(['date','code'])
        except:
            res = None
        if format in ['P', 'p', 'pandas', 'pd']:
            return res
        elif format in ['json', 'dict']:
            return QA_util_to_json_from_pandas(res)
        # 多种数据格式
        elif format in ['n', 'N', 'numpy']:
            return numpy.asarray(res)
        elif format in ['list', 'l', 'L']:
            return numpy.asarray(res).tolist()
        else:
            print("QA Error QA_fetch_stock_alpha format parameter %s is none of  \"P, p, pandas, pd , json, dict , n, N, numpy, list, l, L, !\" " % format)
            return None
    else:
        QA_util_log_info(
            'QA Error QA_fetch_stock_alpha data parameter start=%s end=%s is not right' % (start, end))

def QA_fetch_stock_shares(code, start, end=None, format='pd',type = 'day', collections=DATABASE.stock_shares):
    '获取股票日线'
    #code= [code] if isinstance(code,str) else code
    # code checking
    code = QA_util_code_tolist(code)

    if QA_util_date_valid(end):

        __data = []
        if type == 'day':
            cursor = collections.find({
                'code': {'$in': code}, "begin_date": {
                    "$lte": QA_util_date_stamp(end),
                    "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
            res = pd.DataFrame([item for item in cursor])
        elif type == 'crawl':
            cursor = collections.find({
                'code': {'$in': code}, "crawl_date": {
                    "$lte": QA_util_date_stamp(end),
                    "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
            res = pd.DataFrame([item for item in cursor])
        else:
            print("type must be one of [day, crawl]")

        try:
            res = res.ix[:, ['begin_date','code','crawl_date','exe_shares',
                             'nontra_ashares','nontra_bshares','pre_shares','reason',
                             'send_date','total_shares','tra_ashares','tra_bshares','tra_hshares']]
            res['begin_date'] = res['begin_date'].apply(lambda x: datetime.datetime.fromtimestamp(math.floor(x)))
            res['crawl_date'] = res['crawl_date'].apply(lambda x: datetime.datetime.fromtimestamp(math.floor(x)))
        except:
            res = None
        if format in ['P', 'p', 'pandas', 'pd']:
            return res
        elif format in ['json', 'dict']:
            return QA_util_to_json_from_pandas(res)
        # 多种数据格式
        elif format in ['n', 'N', 'numpy']:
            return numpy.asarray(res)
        elif format in ['list', 'l', 'L']:
            return numpy.asarray(res).tolist()
        else:
            print("QA Error QA_fetch_stock_shares format parameter %s is none of  \"P, p, pandas, pd , json, dict , n, N, numpy, list, l, L, !\" " % format)
            return None
    else:
        QA_util_log_info(
            'QA Error QA_fetch_stock_shares data parameter start=%s end=%s is not right' % (start, end))


def QA_fetch_financial_report_wy(code, start_date = None, end_date = None, type ='report', ltype='EN', db=DATABASE):
    """获取专业财务报表

    Arguments:
        code {[type]} -- [description]
        report_date {[type]} -- [description]

    Keyword Arguments:
        ltype {str} -- [description] (default: {'EN'})
        db {[type]} -- [description] (default: {DATABASE})

    Raises:
        e -- [description]

    Returns:
        pd.DataFrame -- [description]
    """

    if code is None:
        code = list(QA_fetch_future_list_adv()['code'])

    if isinstance(code, str):
        code = [code]

    if start_date is None:
        start = '1995-01-01'
    else:
        start = start_date

    if end_date is None:
        end = QA_util_today_str()
    else:
        end = end_date

    collection = db.stock_financial_wy
    num_columns = [item[:3] for item in list(financial_dict.keys())]
    CH_columns = [item[3:] for item in list(financial_dict.keys())]
    EN_columns = list(financial_dict.values())

    try:
        if type == 'report':
            cursor = collection.find({
                'code': {'$in': code}, "report_date": {
                    "$lte": QA_util_date_stamp(end),
                    "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
            data = pd.DataFrame([item for item in cursor])
        elif type == 'crawl':
            cursor = collection.find({
                'code': {'$in': code}, "crawl_date": {
                    "$lte": QA_util_date_stamp(end),
                    "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
            data = pd.DataFrame([item for item in cursor])
        else:
            print("type must be one of [report, crawl]")

        if len(data) > 0:
            res_pd = pd.DataFrame(data)
            res_pd = res_pd[list(dict2.keys())]
            res_pd.columns = res_pd.columns.map(lambda x: dict2[x])
            res_pd['netProAftExtrGainLoss']=res_pd['netProfitsBelToParComOwner'] - res_pd['nonOperatingIncome']

            """
            if ltype in ['CH', 'CN']:

                cndict = dict(zip(num_columns, CH_columns))
                cndict['283']='283'
                try:
                    cndict['284'] = '284'
                    cndict['285'] = '285'
                    cndict['286'] = '286'
                except:
                    pass
                cndict['_id']='_id'
                cndict['code']='code'
                cndict['report_date']='report_date'
                cndict['crawl_date']='crawl_date'
                res_pd.columns = res_pd.columns.map(lambda x: cndict[x])
            elif ltype is 'EN':
                endict=dict(zip(num_columns,EN_columns))
                endict['283']='283'
                try:
                    endict['284'] = '284'
                    endict['285'] = '285'
                    endict['286'] = '286'
                except:
                    pass
                endict['_id']='_id'
                endict['code']='code'
                endict['report_date']='report_date'
                endict['crawl_date']='crawl_date'
                res_pd.columns = res_pd.columns.map(lambda x: endict[x])
            """
            res_pd['crawl_date'] = res_pd['crawl_date'].apply(lambda x: datetime.datetime.fromtimestamp(math.floor(x)))
            res_pd['report_date'] = res_pd['report_date'].apply(lambda x: datetime.datetime.fromtimestamp(math.floor(x)))
            return res_pd.replace(-4.039810335e+34, numpy.nan).set_index(['report_date', 'code'], drop=False)
        else:
            return None
    except Exception as e:
        raise e

def QA_fetch_stock_technical_index(code, start, end=None, type='day', format='pd'):
    '获取股票日线'
    #code= [code] if isinstance(code,str) else code
    # code checking
    if type == 'day':
        collections=DATABASE.stock_technical_index
    elif type == 'week':
        collections=DATABASE.stock_technical_week
    elif type == 'month':
        collections=DATABASE.stock_technical_month
    else:
        print("type should be in ['day', 'week', 'month']")
    code = QA_util_code_tolist(code)
    if QA_util_date_valid(end):

        __data = []
        cursor = collections.find({
            'code': {'$in': code}, "date_stamp": {
                "$lte": QA_util_date_stamp(end),
                "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
        #res=[QA_util_dict_remove_key(data, '_id') for data in cursor]

        res = pd.DataFrame([item for item in cursor])
        try:
            res = res.drop_duplicates(
                (['code', 'date']))
            res['date'] = res['date'].apply(lambda x: str(x)[0:10])
            res = res.drop(['date_stamp'],axis=1).set_index(['date','code'])
        except:
            res = None
        if format in ['P', 'p', 'pandas', 'pd']:
            return res
        elif format in ['json', 'dict']:
            return QA_util_to_json_from_pandas(res)
        # 多种数据格式
        elif format in ['n', 'N', 'numpy']:
            return numpy.asarray(res)
        elif format in ['list', 'l', 'L']:
            return numpy.asarray(res).tolist()
        else:
            print("QA Error QA_fetch_stock_alpha format parameter %s is none of  \"P, p, pandas, pd , json, dict , n, N, numpy, list, l, L, !\" " % format)
            return None
    else:
        QA_util_log_info(
            'QA Error QA_fetch_stock_alpha data parameter start=%s end=%s is not right' % (start, end))

def QA_fetch_stock_financial_percent(code, start, end=None, format='pd', collections=DATABASE.stock_financial_percent):
    '获取股票日线'
    #code= [code] if isinstance(code,str) else code
    # code checking
    code = QA_util_code_tolist(code)

    if QA_util_date_valid(end):

        __data = []
        cursor = collections.find({
            'code': {'$in': code}, "date_stamp": {
                "$lte": QA_util_date_stamp(end),
                "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
        #res=[QA_util_dict_remove_key(data, '_id') for data in cursor]

        res = pd.DataFrame([item for item in cursor])
        try:
            res = res.drop_duplicates(
                (['code', 'date'])).drop(['date_stamp'],axis=1).set_index(['date','code'])
        except:
            res = None
        if format in ['P', 'p', 'pandas', 'pd']:
            return res
        elif format in ['json', 'dict']:
            return QA_util_to_json_from_pandas(res)
        # 多种数据格式
        elif format in ['n', 'N', 'numpy']:
            return numpy.asarray(res)
        elif format in ['list', 'l', 'L']:
            return numpy.asarray(res).tolist()
        else:
            print("QA Error QA_fetch_stock_financial_percent format parameter %s is none of  \"P, p, pandas, pd , json, dict , n, N, numpy, list, l, L, !\" " % format)
            return None
    else:
        QA_util_log_info(
            'QA Error QA_fetch_stock_financial_percent data parameter start=%s end=%s is not right' % (start, end))

@time_this_function
def QA_fetch_stock_quant_data(code, start, end=None, format='pd', collections=DATABASE.stock_quant_data):
    '获取股票日线'
    #code= [code] if isinstance(code,str) else code
    # code checking
    code = QA_util_code_tolist(code)
    financial = DATABASE.stock_quant_data_financial
    index = DATABASE.stock_quant_data_index
    week = DATABASE.stock_quant_data_week
    alpha = DATABASE.stock_quant_data_alpha
    block = QA.QA_fetch_stock_block(code).reset_index(drop=True).drop_duplicates()
    block = pd.crosstab(block['code'],block['blockname'])
    if QA_util_date_valid(end):

        __data = []
        cursor = financial.find({
            'code': {'$in': code}, "date_stamp": {
                "$lte": QA_util_date_stamp(end),
                "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
        financial_res = pd.DataFrame([item for item in cursor])

        cursor = index.find({
            'code': {'$in': code}, "date_stamp": {
                "$lte": QA_util_date_stamp(end),
                "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
        index_res = pd.DataFrame([item for item in cursor])

        cursor = week.find({
            'code': {'$in': code}, "date_stamp": {
                "$lte": QA_util_date_stamp(end),
                "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
        week_res = pd.DataFrame([item for item in cursor])

        cursor = alpha.find({
            'code': {'$in': code}, "date_stamp": {
                "$lte": QA_util_date_stamp(end),
                "$gte": QA_util_date_stamp(start)}}, {"_id": 0}, batch_size=10000)
        alpha_res = pd.DataFrame([item for item in cursor])
        try:
            res = financial_res.drop_duplicates(
                (['code', 'date'])).drop(['date_stamp'],axis=1).set_index(['date','code']).join(
                index_res.drop_duplicates(
                    (['code', 'date'])).drop(['date_stamp'],axis=1).set_index(['date','code'])).join(
                week_res.drop_duplicates(
                    (['code', 'date'])).drop(['date_stamp'],axis=1).set_index(['date','code'])).join(
                alpha_res.drop_duplicates(
                    (['code', 'date'])).drop(['date_stamp'],axis=1).set_index(['date','code'])).join(
                block, on = 'code', lsuffix='_caller', rsuffix='_other')
            for columnname in res.columns:
                if res[columnname].dtype == 'float64':
                    res[columnname]=res[columnname].astype('float16')
                if res[columnname].dtype == 'float32':
                    res[columnname]=res[columnname].astype('float16')
                if res[columnname].dtype == 'int64':
                    res[columnname]=res[columnname].astype('int8')
                if res[columnname].dtype == 'int32':
                    res[columnname]=res[columnname].astype('int8')
                if res[columnname].dtype == 'int16':
                    res[columnname]=res[columnname].astype('int8')
        except:
            res = None
        if format in ['P', 'p', 'pandas', 'pd']:
            return res
        elif format in ['json', 'dict']:
            return QA_util_to_json_from_pandas(res)
        # 多种数据格式
        elif format in ['n', 'N', 'numpy']:
            return numpy.asarray(res)
        elif format in ['list', 'l', 'L']:
            return numpy.asarray(res).tolist()
        else:
            print("QA Error QA_fetch_stock_quant_data format parameter %s is none of  \"P, p, pandas, pd , json, dict , n, N, numpy, list, l, L, !\" " % format)
            return None
    else:
        QA_util_log_info(
            'QA Error QA_fetch_stock_quant_data date parameter start=%s end=%s is not right' % (start, end))

def QA_fetch_stock_target(codes, start_date, end_date, type='close'):
    end = QA_util_get_pre_trade_date(end_date,-5)
    rng1 = pd.Series(pd.date_range(start_date, end_date, freq='D')).apply(lambda x: str(x)[0:10])
    data = QA.QA_fetch_stock_day_adv(codes,start_date,end)
    market = QA.QA_fetch_index_day(['000905'],start_date,end,format='pd')['close'].reset_index()
    market = index_pct(market)[['date','INDEX_TARGET','INDEX_TARGET3','INDEX_TARGET4','INDEX_TARGET5','INDEX_TARGET10']]
    res1 = data.to_qfq().data
    res1.columns = [x + '_qfq' for x in res1.columns]
    data = data.data.join(res1).fillna(0).reset_index()
    res = data.groupby('code').apply(pct, type=type)[['date','code','OPEN_MARK','PASS_MARK',
                                                    'TARGET','TARGET3','TARGET4','TARGET5',
                                                      'TARGET10','AVG_TARGET']].set_index(['date','code'])
    res = res.reset_index()
    res = pd.merge(res,market,on='date')
    res['date'] = res['date'].apply(lambda x: str(x)[0:10])
    res = res.set_index(['date','code']).loc[rng1]
    res['INDEX_TARGET'] = res['TARGET'] - res['INDEX_TARGET']
    res['INDEX_TARGET3'] = res['TARGET3'] - res['INDEX_TARGET3']
    res['INDEX_TARGET4'] = res['TARGET4'] - res['INDEX_TARGET4']
    res['INDEX_TARGET5'] = res['TARGET5'] - res['INDEX_TARGET5']
    res['INDEX_TARGET10'] = res['TARGET10'] - res['INDEX_TARGET10']
    for columnname in res.columns:
        if res[columnname].dtype == 'float64':
            res[columnname]=res[columnname].astype('float16')
        if res[columnname].dtype == 'int64':
            res[columnname]=res[columnname].astype('int8')
    return(res)

def QA_fetch_stock_quant_pre(code, start, end=None, format='pd'):
    res = QA_fetch_stock_quant_data(code, start, end)
    target = QA_fetch_stock_target(code, start, end)
    res = res.join(target)
    if format in ['P', 'p', 'pandas', 'pd']:
        return res
    elif format in ['json', 'dict']:
        return QA_util_to_json_from_pandas(res)
        # 多种数据格式
    elif format in ['n', 'N', 'numpy']:
        return numpy.asarray(res)
    elif format in ['list', 'l', 'L']:
        return numpy.asarray(res).tolist()
    else:
        print("QA Error QA_fetch_stock_quant_data format parameter %s is none of  \"P, p, pandas, pd , json, dict , n, N, numpy, list, l, L, !\" " % format)
        return None

def QA_fetch_financial_code(N=10):
    START_DATE = QA_util_get_pre_trade_date(QA_util_today_str(),N)
    code = list(QA_fetch_stock_financial_calendar(QA.QA_fetch_stock_list_adv().code.tolist(),START_DATE)['code'])
    market_day = pd.DataFrame(QA_fetch_stock_basic_info_tushare())[['code','timeToMarket']].set_index('code')
    market_day['TM'] = market_day['timeToMarket'].apply(lambda x:str(QA_util_add_months(QA_util_date_int2str(int(x)),0) if x >0 else None)[0:10])
    code = list(market_day[market_day['TM']>= START_DATE]['code']) + code
    return(code)