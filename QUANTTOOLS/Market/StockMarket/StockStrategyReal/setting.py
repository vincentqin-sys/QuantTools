#coding :utf-8

working_dir = 'D:\\model\\current'
percent = 1
exceptions = None
top = 20

stock_day_set = ['ALPHA_067',
                 'MA180_HR',
                 'MACD_TR',
                 'DIF',
                 'AD_C',
                 'MACD',
                 'PB_30PCT',
                 'ALPHA_089',
                 'MA60',
                 'PB_30UP',
                 'SHORT60',
                 'TERNS',
                 'CROSS_SC',
                 'LONG180_HR',
                 'AVG60',
                 'ADDI_C',
                 'DEA',
                 'ALPHA_169',
                 'ADX',
                 'RSI1']

stock_hour_set = ['RSI1_HR',
                  'DIF_HR',
                  'RSI2_HR',
                  'BIAS3_HR',
                  'TERNS_HR',
                  'MACD_TR_HR',
                  'MACD_HR',
                  'MAOSC_HR',
                  'MA60_HR',
                  'SHORT60_HR',
                  'AD_C_HR',
                  'DDD_HR',
                  'BOLL_HR',
                  'DI_M_HR',
                  'DEA_HR',
                  'MA20_HR',
                  'CROSS_SC_HR',
                  'LONG_AMOUNT_HR',
                  'ROCMA_HR',
                  'ADX_HR']

stock_min_set = ['RSI1_15M',
                 'BIAS3_15M',
                 'MAOSC_15M',
                 'DIF_15M',
                 'TERNS_15M',
                 'MA60_15M',
                 'SHORT60_15M',
                 'MACD_15M',
                 'ROCMA_15M',
                 'MACD_TR_15M',
                 'BOLL_15M',
                 'MA20_15M',
                 'DDD_15M',
                 'DEA_15M',
                 'LONG_AMOUNT_15M',
                 'DI_M_15M',
                 'LONG120_15M',
                 'SHORT20_15M',
                 'CROSS_SC_15M',
                 'ADX_15M']

index_day_set = ['RSI2',
                 'MACD_TR',
                 'MA120_HR',
                 'DIF',
                 'MA60',
                 'TERNS',
                 'AD_C',
                 'MACD',
                 'BIAS3',
                 'RSI1',
                 'LONG_AMOUNT',
                 'DDD',
                 'AMA',
                 'ADDI_C',
                 'BOLL',
                 'OSC',
                 'MAOSC',
                 'LONG60',
                 'RSI3',
                 'SHORT60']

index_hour_set = ['RSI1_HR',
                  'BIAS3_HR',
                  'TERNS_HR',
                  'MAOSC_HR',
                  'MACD_TR_HR',
                  'MA60_HR',
                  'SHORT60_HR',
                  'AD_C_HR',
                  'MACD_HR',
                  'DI_M_HR',
                  'ROCMA_HR',
                  'BOLL_HR',
                  'DIF_HR',
                  'LONG_AMOUNT_HR',
                  'DDD_HR',
                  'AMA_HR',
                  'MA20_HR',
                  'SHORT20_HR',
                  'OSC_HR',
                  'MA60_C_HR']