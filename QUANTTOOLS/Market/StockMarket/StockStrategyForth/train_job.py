
from QUANTTOOLS.Market.StockMarket.StockStrategyForth.train import train
from QUANTTOOLS.Market.StockMarket.StockStrategyForth.running import predict
from QUANTTOOLS.Market.StockMarket.StockStrategyForth.setting import working_dir

from QUANTAXIS.QAUtil.QADate_trade import QA_util_if_trade,QA_util_get_real_date

from datetime import datetime

def daily_train(trading_date):

    if datetime.strptime(trading_date, "%Y-%m-%d").weekday() == 4:

        if QA_util_if_trade(trading_date):
            pass
        else:
            trading_date = QA_util_get_real_date(trading_date)

        train(trading_date, working_dir=working_dir)
        predict(trading_date)
    else:
        pass


