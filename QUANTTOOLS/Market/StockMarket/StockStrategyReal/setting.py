#coding :utf-8

working_dir = 'D:\\model\\current'
top = 20
percent = 1
exceptions = None

strategy_id = {'account': 'name:client-1',
               'exceptions': None,
               'strategy_id': '机器学习1号',
               'percent': 1,
               'trader_path': None,
               }

stock_xg_set = ['AVG30_RNG',
                 'AVG20_RNG',
                 'AVG60_RNG',
                 'LONG_AMOUNT_HR',
                 'LONG_TR_HR',
                 'ALPHA_154',
                 'WR_WK',
                 'ALPHA_024',
                 'WR',
                 'ASIT',
                 'ALPHA_021',
                 'ALPHA_056',
                 'LONG_TR',
                 'AVG60_TR',
                 'MA_VOL45',
                 'ALPHA_006',
                 'AVG60_C_MARKET',
                 'ADDI_WK',
                 'ALPHA_041',
                 'BIAS2_WK',
                 'MA60_C_HR',
                 'ALPHA_082',
                 'MA30',
                 'ALPHA_057',
                 'MA_VOL60',
                 'SHORT_AMOUNT',
                 'SHORT_TR_HR',
                 'KDJ_K',
                 'PB_60DN',
                 'WR1_WK',
                 'ALPHA_003',
                 'MA10_HR',
                 'ALPHA_042',
                 'MA30_C',
                 'ALPHA_081',
                 'MA10_WK',
                 'ALPHA_067',
                 'SHORT20',
                 'ALPHA_096',
                 'LONG_AMOUNT',
                 'ALPHA_097',
                 'MA60',
                 'ALPHA_170',
                 'WR1',
                 'MTMMA_HR',
                 'ASIT_HR',
                 'MA_VOL30',
                 'SHORT_TR_WK',
                 'GMMA40',
                 'ALPHA_035',
                 'RSI2_C_HR',
                 'CDLBELTHOLD_WK',
                 'MA15_C_HR',
                 'RSI2',
                 'AD_WK',
                 'MACD_TR_WK',
                 'MA_VOL35',
                 'GMMA_VOL35_HR',
                 'GMMA_VOL30_HR',
                 'AVG5_TOR',
                 'ALPHA_076',
                 'MA_VOL50',
                 'DAYS',
                 'CDLSHORTLINE_WK',
                 'MR_WK',
                 'RSI1_C_HR',
                 'MA_VOL20',
                 'PT',
                 'RNG_90',
                 'PE_90UP',
                 'ALPHA_100',
                 'MA_VOL15_WK',
                 'RSI3_C_HR',
                 'MA_VOL8_WK',
                 'ADTM_CROSS2_WK',
                 'ALPHA_070',
                 'MA45_HR',
                 'MS_WK',
                 'ALPHA_098',
                 'AVG20',
                 'ALPHA_062',
                 'CDLDOJI_WK',
                 'WIDTH_WK',
                 'MAOSC_WK',
                 'ALPHA_159',
                 'SS_WK',
                 'GMMA3_HR',
                 'ALPHA_134',
                 'ALPHA_135',
                 'MA_VOL5',
                 'MACD_TR',
                 'MA30_C_HR',
                 'ASIT_WK',
                 'WR2',
                 'ALPHA_047',
                'S_破净资产',
                'S_创业300',
                'S_国证成长',
                'S_百元股',
                'S_基金重仓',
                'S_创质量',
                'S_大盘股',
                'S_300非周',
                'S_低价股',
                'S_高市净率',
                'S_微盘股']

stock_day_set = ['AVG20_RNG',
                'AVG10_RNG',
                'AVG30_RNG',
                'ALPHA_174',
                'OSC',
                'ALPHA_167',
                'AVG60_RNG',
                'AVG60_C_MARKET',
                'RSI2',
                'AVG60',
                'MAMT_60',
                'LB',
                'RNG_90',
                'RSI1',
                'ALPHA_052',
                'MA50',
                'PB',
                'MA40',
                'ALPHA_067',
                'MA_VOL50',
                'MA45',
                'AD_WK',
                'SS',
                'MA60_C_HR',
                'ADDI_WK',
                'WR_HR',
                'KDJ_D',
                'UB_WK',
                'WR',
                'WR_WK',
                'MA_VOL40_HR',
                'ALPHA_163',
                'ALPHA_098',
                'SS_WK',
                'RNG_20',
                'ALPHA_063',
                'ALPHA_159',
                'RNG_60',
                'MAMT_90',
                'MTM_WK',
                'BOLL',
                'AVG30',
                'WR1',
                'LAG60',
                'PB_60UP',
                'BIAS1',
                'BIAS2_WK',
                'ALPHA_047',
                'ALPHA_076',
                'PEEGL_TTM',
                'LAG',
                'ALPHA_068',
                'MA30',
                'ALPHA_089',
                'MA60',
                'BIAS3_HR',
                'MA8_HR',
                'MA60_C',
                'MTMMA_HR',
                'ALPHA_041',
                'MAMT_20',
                'CCI_CROSS4',
                'TOTALPROFITINRATE',
                'DIF_HR',
                'PS_30DN',
                'ADTM',
                'BIAS3',
                'ALPHA_006',
                'MAMT_30',
                'MA_VOL40',
                'PE_TTM',
                'ALPHA_072',
                'GMMA_VOL5',
                'MAADTM_HR',
                'ALPHA_103',
                'WIDTH',
                'MAOSC_WK',
                'ALPHA_020',
                'PS_60UP',
                'DDD',
                'LONG60V_HR',
                 'S_破净资产',
                 'S_创业300',
                 'S_国证成长',
                 'S_百元股',
                 'S_基金重仓',
                 'S_创质量',
                 'S_大盘股',
                 'S_300非周',
                 'S_低价股',
                 'S_高市净率',
                 'S_微盘股']

index_xg_set = ['MTM_HR',
                 'MA5',
                 'SKDJ_TR',
                 'MACD_TR_WK',
                 'GMMA3',
                 'LONG60_HR',
                 'ADDI_HR',
                 'RSI2_HR',
                 'SKDJ_CROSS1_WK',
                 'RSI2_WK',
                 'MA_VOL5_C_WK',
                 'RSI1_WK',
                 'GMMA35_HR',
                 'MA12_HR',
                 'SHORT_TR_WK',
                 'RSI1_C_WK',
                 'OSC_CROSS1_WK',
                 'SAR_MARK',
                 'BOLL',
                 'CDLADVANCEBLOCK_WK',
                 'DDD_HR',
                 'RSI3',
                 'MA_VOL5_WK',
                 'CDLHANGINGMAN_WK',
                 'RSI3_C_WK',
                 'GMMA10',
                 'SHORT10_WK',
                 'MA5_C_WK',
                 'SHORT60_HR',
                'S_破净资产',
                'S_创业300',
                'S_国证成长',
                'S_百元股',
                'S_基金重仓',
                'S_创质量',
                'S_大盘股',
                'S_300非周',
                'S_低价股',
                'S_高市净率',
                'S_微盘股']

stock_xg_nn = ['AVG20_RNG',
               'AVG10_RNG',
               'AVG30_RNG',
               'AD_WK',
               'RSI1',
               'BIAS3_WK',
               'RSI1_WK',
               'AVG60_RNG',
               'MAMT_60',
               'MA60',
               'ALPHA_072',
               'ALPHA_047',
               'MA45',
               'PB',
               'MA_VOL60',
               'ALPHA_082',
               'ADDI_WK',
               'MA40',
               'GMMA_VOL3',
               'ALPHA_174',
               'RSI3',
               'WR',
               'ALPHA_089',
               'MA10',
               'ALPHA_057',
               'MAMT_30',
               'MA50',
               'RSI2',
               'RNG_90',
               'KDJ_K',
               'SHORT60_HR',
               'MA35',
               'ALPHA_067',
               'VSTD_WK',
               'SR',
               'ALPHA_158',
               'RSI2_WK',
               'PS_30DN',
               'ALPHA_003',
               'SHORT60V_HR',
               'WR_WK',
               'MA50_HR',
               'WS',
               'ALPHA_042',
               'RNG_60',
               'WIDTH_WK',
               'MTMMA_WK',
               'SS_WK',
               'ALPHA_101',
               'ALPHA_076',
               'MAMT_20',
               'AVG60',
               'PS_60UP',
               'TOTAL_MARKET',
               'ALPHA_163',
               'ALPHA_035',
               'MA_VOL50',
               'ALPHA_103',
               'MA60_HR',
               'GMMA40',
               'ALPHA_041',
               'WIDTH_HR',
               'LONG_AMOUNT',
               'PB_60UP',
               'RSI2_HR',
               'PS_30VAL',
               'SHORT_AMOUNT',
               'ALPHA_062',
               'ALPHA_013',
               'SHORT10_HR',
               'BIAS3',
               'MA30',
               'ALPHA_118',
               'GMMA3_C',
               'DEA_WK',
               'MAMT_10',
               'ALPHA_024',
               'LB',
               'BIAS1_HR',
               'RNG_10',
               'DAYS',
               'ALPHA_006',
               'WR1_WK',
               'GMMA15_C_WK',
               'RNG_20',
               'PS_60VAL',
               'GMMA10',
               'S_破净资产',
               'S_创业300',
               'S_国证成长',
               'S_百元股',
               'S_基金重仓',
               'S_创质量',
               'S_大盘股',
               'S_300非周',
               'S_低价股',
               'S_高市净率',
               'S_微盘股']

stock_day_nn = ['AVG20_RNG',
                'AVG30_RNG',
                'OSC',
                'ALPHA_167',
                'AVG60_RNG',
                'MAMT_90',
                'AVG10_RNG',
                'MA40',
                'ALPHA_174',
                'MA60',
                'ALPHA_067',
                'RSI1',
                'RSI2',
                'BOLL',
                'RNG_90',
                'PB',
                'AVG60',
                'RNG_20',
                'MAMT_60',
                'ADDI_WK',
                'PM',
                'LB',
                'MA50',
                'WR_HR',
                'KDJ_D',
                'ALPHA_163',
                'WR_WK',
                'SS_WK',
                'AVG20',
                'AD_WK',
                'ALPHA_047',
                'MAMT_30',
                'MA60_C_HR',
                'MA45',
                'LAG5',
                'SS',
                'RSI1_WK',
                'WR',
                'RNG_60',
                'ALPHA_118',
                'MA30',
                'ALPHA_076',
                'PE_TTM',
                'DIF',
                'STOCK_TYPE',
                'BIAS1_HR',
                'ALPHA_089',
                'LONG60',
                'MA_VOL20',
                'ALPHA_098',
                'LONG_AMOUNT_HR',
                'ALPHA_126',
                'BIAS3_WK',
                'GMMA5_HR',
                'ALPHA_159',
                'AVG30',
                'ALPHA_041',
                'ALPHA_189',
                'ALPHA_187',
                'ALPHA_012',
                'DEA_HR',
                'PS_60UP',
                'WIDTH',
                'GMMA35',
                'ALPHA_008',
                'DDD_HR',
                'ALPHA_006',
                'ALPHA_019',
                'WIDTH_WK',
                'TOTAL_MARKET',
                'DEA',
                'ALPHA_021',
                'BIAS2_WK',
                'PE_RATE',
                'SKDJ_K_HR',
                'AVG30_TOR',
                'GMMA30',
                'PB_60DN',
                'MA_VOL60_HR',
                'S_破净资产',
                'S_创业300',
                'S_国证成长',
                'S_百元股',
                'S_基金重仓',
                'S_创质量',
                'S_大盘股',
                'S_300非周',
                'S_低价股',
                'S_高市净率',
                'S_微盘股']

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

index_hour_set = ['MA3_HR',
                  'SKDJ_D_HR',
                  'GMMA8_HR',
                  'KDJ_D_HR',
                  'RSI1_C_HR',
                  'MA5_HR',
                  'WR2_HR',
                  'SKDJ_CROSS2_HR',
                  'GMMA3_D_HR',
                  'SKDJ_TR_HR',
                  'SKDJ_CROSS1_HR',
                  'WR1_HR',
                  'KDJ_CROSS1_HR',
                  'GMMA10_HR',
                  'SKDJ_K_HR',
                  'KDJ_CROSS2_HR',
                  'MA5_D_HR',
                  'WR_CROSS2_HR',
                  'GMMA3_C_HR',
                  'GMMA5_HR',
                  'RSI2_C_HR',
                  'KDJ_K_HR',
                  'MA_VOL3_HR',
                  'GMMA_VOL3_HR',
                  'MA_VOL35_HR',
                  'GMMA_VOL3_D_HR',
                  'UB_HR',
                  'MS_HR',
                  'KDJ_J_HR',
                  'WR_CROSS1_HR']

block_set = ['ALPHA_067',
             'OSC_HR',
             'AVG30_RNG',
             'MA50',
             'DMA_CROSS1',
             'MA30_WK',
             'AVG10_RNG',
             'SKDJ_K1',
             'GMMA3_WK',
             'LONG_AMOUNT_WK',
             'SKDJ_K',
             'PEEGL_TTM',
             'LAG3',
             'MA40_WK',
             'NEG60_RATE',
             'SHORT_AMOUNT_WK',
             'ALPHA_060',
             'ALPHA_159',
             'MTM_HR',
             'ALPHA_065',
             'MIKE_WSJC',
             'MAMT_20',
             'MA60_D_WK',
             'LONG_AMOUNT',
             'ALPHA_028',
             'S_医疗保健',
             'PS_30UP',
             'KDJ_D_WK',
             'ALPHA_109',
             'MA_VOL40',
             'SKDJ_K6',
             'MA5_WK',
             'KDJ_K_HR',
             'S_燃料电池',
             'PB_60DN',
             'AVG60',
             'RSV_WK',
             'ALPHA_014',
             'ALPHA_015',
             'AVG20_TOR',
             'GMMA5_WK',
             'PRICE_PCG_WK',
             'ALPHA_079',
             'S_痘病毒',
             'OSC_WK',
             'PE_60VAL',
             'SHA_LOW_WK',
             'SKDJ_K_WK1',
             'GMMA3',
             'GMMA8',
             'GMMA8_HR',
             'SKDJ_D',
             'MA_VOL50_WK',
             'SKDJ_K_WK6',
             'MA_VOL45',
             'BBI_HR',
             'AMA',
             'SKDJ_TR_WK1',
             'TOTALPROFITINRATE',
             'AVG5_TOR',
             'MA_VOL60_WK',
             'BODY_ABS_WK',
             'ALPHA_004',
             'SR_HR',
             'PB_90VAL',
             'AVG20_C_MARKET',
             'ALPHA_031',
             'PE_90UP',
             'MA_VOL45_WK',
             'ROCMA_HR',
             'MA_VOL50',
             'VRSI',
             'GMMA5_HR',
             'ALPHA_120',
             'SS_WK',
             'ALPHA_043',
             'MACD_HR',
             'RNG_90',
             'LAG5',
             'SHORT_AMOUNT_HR',
             'OBV_HR',
             'ALPHA_080',
             'LAG10',
             'S_腾讯济安',
             'ASIT_WK',
             'RNG_20',
             'LB_HR',
             'DI_M',
             'RSI3',
             'GMMA_VOL10_HR',
             'DI1',
             'MA30_D_WK',
             'PE_30UP',
             'S_央企改革',
             'LONG60V_HR',
             'KDJ_J_WK',
             'CCI',
             'ROE',
             'WR1_WK']