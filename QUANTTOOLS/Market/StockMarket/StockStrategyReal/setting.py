#coding :utf-8

working_dir = 'D:\\model\\current'
percent = 1
exceptions = None
top = 20

stock_xg_set = ['ALPHA_174',
                'ATR_HR',
                'LONG_WK',
                'OSC',
                'BOLL',
                'SS_WK',
                'PB',
                'BIAS3',
                'ALPHA_067',
                'AVG20',
                'AVG60',
                'WR_WK',
                'MA_VOL60',
                'AD_WK',
                'WR',
                'ADDI_WK',
                'PB_60VAL',
                'AVG60_RNG',
                'MA60',
                'LONG60',
                'DDD',
                'ALPHA_035',
                'ALPHA_052',
                'ALPHA_024',
                'ALPHA_076',
                'BIAS2_WK',
                'ATRR_HR',
                'MA50',
                'WR1',
                'MAMT_30',
                'ALPHA_139',
                'GMMA35',
                'BOLL_WK',
                'DIF_HR',
                'VSTD_WK',
                'RSI2',
                'ALPHA_083',
                'ALPHA_089',
                'MA_VOL50',
                'ALPHA_065',
                'MA60_HR',
                'ALPHA_133',
                'VR_HR',
                'RNG_90',
                'UB',
                'CDLBELTHOLD_WK',
                'ALPHA_062',
                'WR1_WK',
                'ALPHA_042',
                'KDJ_D_WK',
                'MA15',
                'LB_WK',
                'RNG_30',
                'MA10_WK',
                'DEA_HR',
                'ALPHA_072',
                'ALPHA_057',
                'RSI2_WK',
                'ALPHA_003',
                'PS_10VAL',
                'AVG30_TOR',
                'KDJ_D_HR',
                'MAMT_60',
                'ALPHA_047',
                'ROC',
                'RSV_WK',
                'SHORT60V_HR',
                'MA_VOL15_WK',
                'TRA_RATE',
                'MA_VOL35',
                'ALPHA_046',
                'SKDJ_D',
                'PS_60DN',
                'RNG_60',
                'SR_WK',
                'SHORT60_HR',
                'MAMT_10',
                'ALPHA_153',
                'WIDTH_HR',
                'BBI',
                'MA_VOL20_WK',
                'ALPHA_163',
                'KDJ_J',
                'PS_30UP',
                'PRICE_PCG_HR',
                'CDLSHORTLINE_WK',
                'MA12_WK',
                'TOTAL_MARKET',
                'MA_VOL5_WK',
                'GMMA_VOL3_WK',
                'PS_20VAL',
                'NEG90_RT',
                'CCI',
                'KDJ_K',
                'AMT_60',
                'PS_60UP',
                'PB_90VAL',
                'MACD_HR',
                'SHA_UP_WK',
                'ALPHA_170']

stock_day_set = ['CCI_HR',
                 'MA3',
                 'ALPHA_021',
                 'KDJ_K_HR',
                 'MA15_HR',
                 'LAG2',
                 'GMMA30_HR',
                 'SKDJ_D',
                 'WR1_HR',
                 'MA5',
                 'AVG5',
                 'BIAS1',
                 'KDJ_D_HR',
                 'MIKE_BOLL_HR',
                 'SKDJ_K_HR',
                 'BOLL_HR',
                 'KDJ_CROSS2',
                 'KDJ_J_HR',
                 'AVG10_C_MARKET',
                 'WR2',
                 'KDJ_CROSS1',
                 'KDJ_D',
                 'MA8',
                 'MA30_D_HR',
                 'GMMA10',
                 'GMMA3_HR',
                 'LAG3',
                 'GMMA8',
                 'GMMA35_HR',
                 'WR1']

stock_hour_set = ['MA3_HR',
                  'SKDJ_D_HR',
                  'GMMA8_HR',
                  'GMMA5_HR',
                  'MA5_HR',
                  'WR2_HR',
                  'KDJ_CROSS1_HR',
                  'KDJ_CROSS2_HR',
                  'SKDJ_CROSS2_HR',
                  'SKDJ_CROSS1_HR',
                  'WR1_HR',
                  'GMMA10_HR',
                  'SKDJ_TR_HR',
                  'GMMA3_D_HR',
                  'SKDJ_K_HR',
                  'KDJ_D_HR',
                  'MA5_D_HR',
                  'WR_CROSS1_HR',
                  'WR_CROSS2_HR',
                  'RSI1_C_HR',
                  'MA30_C_HR',
                  'SR_HR',
                  'KDJ_J_HR',
                  'KDJ_K_HR',
                  'VSTD_HR',
                  'CCI_HR',
                  'MA_VOL3_HR',
                  'GMMA_VOL3_C_HR',
                  'SHORT10V_HR',
                  'WS_HR']

index_day_set = ['SKDJ_D',
                 'MA3',
                 'GMMA3_D',
                 'MA5',
                 'GMMA8',
                 'SKDJ_K',
                 'WR2',
                 'RSI1_C',
                 'WR1',
                 'RSI3_C',
                 'GMMA5',
                 'KDJ_CROSS1',
                 'MA5_D',
                 'CDLHARAMI',
                 'BIAS1',
                 'CDLHOMINGPIGEON',
                 'GMMA10',
                 'SKDJ_CROSS2',
                 'SKDJ_TR',
                 'KDJ_CROSS2',
                 'CDLINVERTEDHAMMER',
                 'SKDJ_CROSS1',
                 'MAOSC',
                 'SS',
                 'ROCMA',
                 'LONG60',
                 'SHORT20',
                 'SHORT_AMOUNT',
                 'MR',
                 'KDJ_D']

index_hour_set = ['SKDJ_D_HR',
                  'MA3_HR',
                  'GMMA8_HR',
                  'WR2_HR',
                  'SKDJ_CROSS2_HR',
                  'GMMA3_D_HR',
                  'MA5_HR',
                  'BIAS1_HR',
                  'SKDJ_TR_HR',
                  'WR1_HR',
                  'KDJ_CROSS1_HR',
                  'SKDJ_K_HR',
                  'KDJ_CROSS2_HR',
                  'GMMA10_HR',
                  'GMMA5_HR',
                  'WR_CROSS2_HR',
                  'KDJ_J_HR',
                  'KDJ_K_HR',
                  'WR_CROSS1_HR',
                  'MA5_D_HR',
                  'GMMA_VOL3_D_HR',
                  'SS_HR',
                  'MA8_HR',
                  'DEA_HR',
                  'GMMA3_HR',
                  'SHORT20_HR',
                  'DDD_HR',
                  'MA_VOL20_HR',
                  'CDLRICKSHAWMAN_HR',
                  'CDLMARUBOZU_HR']
