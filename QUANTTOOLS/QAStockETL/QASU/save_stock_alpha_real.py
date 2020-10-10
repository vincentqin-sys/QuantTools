from QUANTAXIS.QAUtil import (DATABASE, QA_util_log_info,QA_util_to_json_from_pandas,QA_util_today_str,QA_util_get_trade_range, QA_util_if_trade,QA_util_code_tolist)
from QUANTTOOLS.QAStockETL.QAFetch import QA_fetch_stock_all,QA_fetch_stock_om_all
from QUANTTOOLS.QAStockETL.QAFetch import (QA_fetch_get_stock_alpha101half_realtime,
                                           QA_fetch_get_stock_alpha191half_realtime)
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import concurrent
import pymongo
import gc

def QA_SU_save_stock_alpha101half_real(code = None, start_date = None, end_date = None, client=DATABASE, ui_log = None, ui_progress = None):
    '''
     save stock_day
    保存财报日历
    历史全部数据
    :return:
    '''
    if end_date is None:
        end_date = QA_util_today_str()

    if start_date is None:
        start_date = '2017-04-10'
    codes = code
    if codes is None:
        codes = list(QA_fetch_stock_om_all()['code'])
        #codes = [codes[i:i+500] for i in range(0,len(codes),500)]

    #deal_date_list = QA_util_get_trade_range(start_date, end_date)

    client.drop_collection('stock_alpha101_real')
    stock_alpha = client.stock_alpha101_real
    stock_alpha.create_index([("code", pymongo.ASCENDING), ("date_stamp", pymongo.ASCENDING)], unique=True)
    err = []

    def __saving_work(code,start,end):
        try:
            QA_util_log_info(
                '##JOB01 Now Saving Stock Alpha101 Half Real==== {}'.format(str(code)), ui_log)
            data = QA_fetch_get_stock_alpha101half_realtime(code,start,end)
            if data is not None:
                stock_alpha.insert_many(QA_util_to_json_from_pandas(data), ordered=False)
                gc.collect()
        except Exception as error0:
            print(error0)
            err.append(str(code))

    executor = ThreadPoolExecutor(max_workers=5)
    # executor.map((__saving_work,  stock_list[i_], coll),URLS)
    res = {
        executor.submit(__saving_work,
                        codes[i_],
                        start_date,
                        end_date)
        for i_ in range(len(codes))
    }

    count = 0
    for i_ in concurrent.futures.as_completed(res):
        QA_util_log_info(
            'The {} of Total {}'.format(count,
                                        len(codes)),
            ui_log=ui_log
        )

        strProgress = 'DOWNLOAD PROGRESS {} '.format(
            str(float(count / len(codes) * 100))[0:5] + '%'
        )
        intProgress = int(count / len(codes) * 10000.0)
        QA_util_log_info(
            strProgress,
            ui_log,
            ui_progress=ui_progress,
            ui_progress_int_value=intProgress
        )
        count = count + 1

    #k=500
    #for i in range(0, len(codes), k):
    #    code = codes[i:i+k]
    #    QA_util_log_info('The {} of Total {}'.format
    #                     ((i +k ), len(codes)))

    #    strProgressToLog = 'DOWNLOAD PROGRESS {}'.format(str(float((i + k) / len(codes) * 100))[0:4] + '%', ui_log)
    #    intProgressToLog = int(float((i + k ) / len(codes) * 100 ))
    #    QA_util_log_info(strProgressToLog, ui_log= ui_log, ui_progress= ui_progress, ui_progress_int_value= intProgressToLog)

    #    __saving_work(code,start_date,end_date)

    if len(err) < 1:
        QA_util_log_info('SUCCESS save Stock Alpha101 Half Real ^_^',  ui_log)
    else:
        QA_util_log_info(' ERROR CODE \n ',  ui_log)
        QA_util_log_info(err, ui_log)

def QA_SU_save_stock_alpha191half_real(code = None, start_date = None, end_date = None, client=DATABASE, ui_log = None, ui_progress = None):
    '''
     save stock_day
    保存财报日历
    历史全部数据
    :return:
    '''
    if end_date is None:
        end_date = QA_util_today_str()

    if start_date is None:
        start_date = '2017-04-10'

    deal_date_list = QA_util_get_trade_range(start_date, end_date)

    codes = code
    if codes is None:
        codes = list(QA_fetch_stock_om_all()['code'])

    client.drop_collection('stock_alpha191_real')
    stock_alpha = client.stock_alpha191_real
    stock_alpha.create_index([("code", pymongo.ASCENDING), ("date_stamp", pymongo.ASCENDING)], unique=True)
    err = []

    def __saving_work(code,date):
        try:
            QA_util_log_info(
                '##JOB01 Now Saving Stock Alpha191 Half Real==== {}'.format(str(date)), ui_log)
            data = QA_fetch_get_stock_alpha191half_realtime(code,date)
            if data is not None:
                stock_alpha.insert_many(QA_util_to_json_from_pandas(data), ordered=False)
                gc.collect()
        except Exception as error0:
            print(error0)
            err.append(str(code))

    for item in deal_date_list:
        QA_util_log_info('The {} of Total {}'.format
                         ((deal_date_list.index(item) +1), len(deal_date_list)))

        strProgressToLog = 'DOWNLOAD PROGRESS {}'.format(str(float((deal_date_list.index(item) +1) / len(deal_date_list) * 100))[0:4] + '%', ui_log)
        intProgressToLog = int(float((deal_date_list.index(item) +1) / len(deal_date_list) * 100))
        QA_util_log_info(strProgressToLog, ui_log= ui_log, ui_progress= ui_progress, ui_progress_int_value= intProgressToLog)
        __saving_work(codes,item)

    if len(err) < 1:
        QA_util_log_info('SUCCESS save Stock Alpha191 Half Real ^_^',  ui_log)
    else:
        QA_util_log_info(' ERROR CODE \n ',  ui_log)
        QA_util_log_info(err, ui_log)
