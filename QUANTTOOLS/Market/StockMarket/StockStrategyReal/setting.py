working_dir = 'D:\\model\\current'
percent = 1
exceptions = None
top = 5

datareal_set = ['TOTAL_MARKET'
    ,'TRA_RATE'
    ,'DAYS'
    ,'AVG5'
    ,'AVG10'
    ,'AVG20'
    ,'AVG30'
    ,'AVG60'
    ,'LAG'
    ,'LAG5'
    ,'LAG10'
    ,'LAG20'
    ,'LAG30'
    ,'LAG60'
    ,'AVG5_TOR'
    ,'AVG20_TOR'
    ,'AVG30_TOR'
    ,'AVG60_TOR'
    ,'GROSSMARGIN'
    ,'NETPROFIT_INRATE'
    ,'OPERATINGRINRATE'
    ,'NETCASHOPERATINRATE'
    ,'PB'
    ,'PBG'
    ,'PC'
    ,'PE_TTM'
    ,'PEEGL_TTM'
    ,'PEG'
    ,'PM'
    ,'PS'
    ,'PSG'
    ,'PT'
    ,'PE_RATE'
    ,'PEEGL_RATE'
    ,'PB_RATE'
    ,'ROE_RATE'
    ,'ROE_RATET'
    ,'ROA_RATE'
    ,'ROA_RATET'
    ,'GROSS_RATE'
    ,'RNG'
    ,'RNG_L'
    ,'RNG_5'
    ,'RNG_10'
    ,'RNG_20'
    ,'RNG_30'
    ,'RNG_60'
    ,'RNG_90'
    ,'AMT_L'
    ,'AMT_5'
    ,'AMT_10'
    ,'AMT_20'
    ,'AMT_30'
    ,'AMT_60'
    ,'AMT_90'
    ,'MAMT_5'
    ,'MAMT_10'
    ,'MAMT_20'
    ,'MAMT_30'
    ,'MAMT_60'
    ,'MAMT_90'
    ,'AVG5_RNG'
    ,'AVG10_RNG'
    ,'AVG20_RNG'
    ,'AVG30_RNG'
    ,'AVG60_RNG'
    ,'ROA'
    ,'ROE'
    ,'AVG5_CR'
    ,'AVG10_CR'
    ,'AVG20_CR'
    ,'AVG30_CR'
    ,'AVG60_CR'
    ,'AVG5_TR'
    ,'AVG10_TR'
    ,'AVG20_TR'
    ,'AVG30_TR'
    ,'AVG60_TR'
    ,'TOTALPROFITINRATE'
    ,'VR'
    ,'VRSI'
    ,'VRSI_C'
    ,'VSTD'
    ,'BOLL'
    ,'UB'
    ,'LB'
    ,'WIDTH'
    ,'WR'
    ,'MR'
    ,'SR'
    ,'WS'
    ,'MS'
    ,'SS'
    ,'MIKE_WRSC'
    ,'MIKE_WRJC'
    ,'MIKE_WSSC'
    ,'MIKE_WSJC'
    ,'MIKE_TR'
    ,'MIKE_BOLL'
    ,'ASI'
    ,'ASIT'
    ,'OBV'
    ,'OBV_C'
    ,'PVT'
    ,'VPT'
    ,'MAVPT'
    ,'VPT_CROSS1'
    ,'VPT_CROSS2'
    ,'VPT_CROSS3'
    ,'VPT_CROSS4'
    ,'KDJ_K'
    ,'KDJ_D'
    ,'KDJ_J'
    ,'KDJ_CROSS1'
    ,'KDJ_CROSS2'
    ,'WR1'
    ,'WR2'
    ,'WR_CROSS1'
    ,'WR_CROSS2'
    ,'ROC'
    ,'ROCMA'
    ,'RSI1'
    ,'RSI2'
    ,'RSI3'
    ,'RSI1_C'
    ,'RSI2_C'
    ,'RSI3_C'
    ,'RSI_CROSS1'
    ,'RSI_CROSS2'
    ,'CCI'
    ,'CCI_CROSS1'
    ,'CCI_CROSS2'
    ,'CCI_CROSS3'
    ,'CCI_CROSS4'
    ,'BIAS1'
    ,'BIAS2'
    ,'BIAS3'
    ,'BIAS_CROSS1'
    ,'BIAS_CROSS2'
    ,'OSC'
    ,'MAOSC'
    ,'OSC_CROSS1'
    ,'OSC_CROSS2'
    ,'OSC_CROSS3'
    ,'OSC_CROSS4'
    ,'ADTM'
    ,'MAADTM'
    ,'ADTM_CROSS1'
    ,'ADTM_CROSS2'
    ,'DIF'
    ,'DEA'
    ,'MACD'
    ,'CROSS_JC'
    ,'CROSS_SC'
    ,'MACD_TR'
    ,'DI1'
    ,'DI2'
    ,'ADX'
    ,'ADXR'
    ,'ADX_C'
    ,'DI_M'
    ,'DI_CROSS1'
    ,'DI_CROSS2'
    ,'ADX_CROSS1'
    ,'ADX_CROSS2'
    ,'DDD'
    ,'AMA'
    ,'DMA_CROSS1'
    ,'DMA_CROSS2'
    ,'MTM'
    ,'MTMMA'
    ,'MTM_CROSS1'
    ,'MTM_CROSS2'
    ,'MTM_CROSS3'
    ,'MTM_CROSS4'
    ,'MA1'
    ,'MA2'
    ,'MA3'
    ,'MA4'
    ,'CHO'
    ,'MACHO'
    ,'CHO_CROSS1'
    ,'CHO_CROSS2'
    ,'BBI'
    ,'BBI_CROSS1'
    ,'BBI_CROSS2'
    ,'MFI'
    ,'MFI_C'
    ,'TR'
    ,'ATR'
    ,'ATRR'
    ,'RSV'
    ,'SKDJ_K'
    ,'SKDJ_D'
    ,'SKDJ_CROSS1'
    ,'SKDJ_CROSS2'
    ,'DDI'
    ,'ADDI'
    ,'AD'
    ,'DDI_C'
    ,'AD_C'
    ,'ADDI_C'
    ,'SHA_LOW'
    ,'SHA_UP'
    ,'BODY'
    ,'BODY_ABS'
    ,'PRICE_PCG'
    ,'MA5'
    ,'MA10'
    ,'MA20'
    ,'MA60'
    ,'MA120'
    ,'MA180'
    ,'CDL2CROWS'
    ,'CDL3BLACKCROWS'
    ,'CDL3INSIDE'
    ,'CDL3LINESTRIKE'
    ,'CDL3OUTSIDE'
    ,'CDL3STARSINSOUTH'
    ,'CDL3WHITESOLDIERS'
    ,'CDLABANDONEDBABY'
    ,'CDLADVANCEBLOCK'
    ,'CDLBELTHOLD'
    ,'CDLBREAKAWAY'
    ,'CDLCLOSINGMARUBOZU'
    ,'CDLCONCEALBABYSWALL'
    ,'CDLCOUNTERATTACK'
    ,'CDLDARKCLOUDCOVER'
    ,'CDLDOJI'
    ,'CDLDOJISTAR'
    ,'CDLDRAGONFLYDOJI'
    ,'CDLENGULFING'
    ,'CDLEVENINGDOJISTAR'
    ,'CDLEVENINGSTAR'
    ,'CDLGAPSIDESIDEWHITE'
    ,'CDLGRAVESTONEDOJI'
    ,'CDLHAMMER'
    ,'CDLHANGINGMAN'
    ,'CDLHARAMI'
    ,'CDLHARAMICROSS'
    ,'CDLHIGHWAVE'
    ,'CDLHIKKAKE'
    ,'CDLHIKKAKEMOD'
    ,'CDLHOMINGPIGEON'
    ,'CDLIDENTICAL3CROWS'
    ,'CDLINNECK'
    ,'CDLINVERTEDHAMMER'
    ,'CDLKICKING'
    ,'CDLKICKINGBYLENGTH'
    ,'CDLLADDERBOTTOM'
    ,'CDLLONGLEGGEDDOJI'
    ,'CDLLONGLINE'
    ,'CDLMARUBOZU'
    ,'CDLMATCHINGLOW'
    ,'CDLMATHOLD'
    ,'CDLMORNINGDOJISTAR'
    ,'CDLMORNINGSTAR'
    ,'CDLONNECK'
    ,'CDLPIERCING'
    ,'CDLRICKSHAWMAN'
    ,'CDLRISEFALL3METHODS'
    ,'CDLSEPARATINGLINES'
    ,'CDLSHOOTINGSTAR'
    ,'CDLSHORTLINE'
    ,'CDLSPINNINGTOP'
    ,'CDLSTALLEDPATTERN'
    ,'CDLSTICKSANDWICH'
    ,'CDLTAKURI'
    ,'CDLTASUKIGAP'
    ,'CDLTHRUSTING'
    ,'CDLTRISTAR'
    ,'CDLUNIQUE3RIVER'
    ,'CDLUPSIDEGAP2CROWS'
    ,'CDLXSIDEGAP3METHODS'
    ,'VR_WK'
    ,'VRSI_WK'
    ,'VRSI_C_WK'
    ,'VSTD_WK'
    ,'BOLL_WK'
    ,'UB_WK'
    ,'LB_WK'
    ,'WIDTH_WK'
    ,'WR_WK'
    ,'MR_WK'
    ,'SR_WK'
    ,'WS_WK'
    ,'MS_WK'
    ,'SS_WK'
    ,'MIKE_WRSC_WK'
    ,'MIKE_WRJC_WK'
    ,'MIKE_WSSC_WK'
    ,'MIKE_WSJC_WK'
    ,'MIKE_TR_WK'
    ,'MIKE_BOLL_WK'
    ,'ASI_WK'
    ,'ASIT_WK'
    ,'OBV_WK'
    ,'OBV_C_WK'
    ,'PVT_WK'
    ,'VPT_WK'
    ,'MAVPT_WK'
    ,'VPT_CROSS1_WK'
    ,'VPT_CROSS2_WK'
    ,'VPT_CROSS3_WK'
    ,'VPT_CROSS4_WK'
    ,'KDJ_K_WK'
    ,'KDJ_D_WK'
    ,'KDJ_J_WK'
    ,'KDJ_CROSS1_WK'
    ,'KDJ_CROSS2_WK'
    ,'WR1_WK'
    ,'WR2_WK'
    ,'WR_CROSS1_WK'
    ,'WR_CROSS2_WK'
    ,'ROC_WK'
    ,'ROCMA_WK'
    ,'RSI1_WK'
    ,'RSI2_WK'
    ,'RSI3_WK'
    ,'RSI1_C_WK'
    ,'RSI2_C_WK'
    ,'RSI3_C_WK'
    ,'RSI_CROSS1_WK'
    ,'RSI_CROSS2_WK'
    ,'CCI_WK'
    ,'CCI_CROSS1_WK'
    ,'CCI_CROSS2_WK'
    ,'CCI_CROSS3_WK'
    ,'CCI_CROSS4_WK'
    ,'BIAS1_WK'
    ,'BIAS2_WK'
    ,'BIAS3_WK'
    ,'BIAS_CROSS1_WK'
    ,'BIAS_CROSS2_WK'
    ,'OSC_WK'
    ,'MAOSC_WK'
    ,'OSC_CROSS1_WK'
    ,'OSC_CROSS2_WK'
    ,'OSC_CROSS3_WK'
    ,'OSC_CROSS4_WK'
    ,'ADTM_WK'
    ,'MAADTM_WK'
    ,'ADTM_CROSS1_WK'
    ,'ADTM_CROSS2_WK'
    ,'DIF_WK'
    ,'DEA_WK'
    ,'MACD_WK'
    ,'CROSS_JC_WK'
    ,'CROSS_SC_WK'
    ,'MACD_TR_WK'
    ,'DI1_WK'
    ,'DI2_WK'
    ,'ADX_WK'
    ,'ADXR_WK'
    ,'ADX_C_WK'
    ,'DI_M_WK'
    ,'DI_CROSS1_WK'
    ,'DI_CROSS2_WK'
    ,'ADX_CROSS1_WK'
    ,'ADX_CROSS2_WK'
    ,'DDD_WK'
    ,'AMA_WK'
    ,'DMA_CROSS1_WK'
    ,'DMA_CROSS2_WK'
    ,'MTM_WK'
    ,'MTMMA_WK'
    ,'MTM_CROSS1_WK'
    ,'MTM_CROSS2_WK'
    ,'MTM_CROSS3_WK'
    ,'MTM_CROSS4_WK'
    ,'MA1_WK'
    ,'MA2_WK'
    ,'MA3_WK'
    ,'MA4_WK'
    ,'CHO_WK'
    ,'MACHO_WK'
    ,'CHO_CROSS1_WK'
    ,'CHO_CROSS2_WK'
    ,'BBI_WK'
    ,'BBI_CROSS1_WK'
    ,'BBI_CROSS2_WK'
    ,'MFI_WK'
    ,'MFI_C_WK'
    ,'TR_WK'
    ,'ATR_WK'
    ,'ATRR_WK'
    ,'RSV_WK'
    ,'SKDJ_K_WK'
    ,'SKDJ_D_WK'
    ,'SKDJ_CROSS1_WK'
    ,'SKDJ_CROSS2_WK'
    ,'DDI_WK'
    ,'ADDI_WK'
    ,'AD_WK'
    ,'DDI_C_WK'
    ,'AD_C_WK'
    ,'ADDI_C_WK'
    ,'SHA_LOW_WK'
    ,'SHA_UP_WK'
    ,'BODY_WK'
    ,'BODY_ABS_WK'
    ,'PRICE_PCG_WK'
    ,'MA5_WK'
    ,'MA10_WK'
    ,'MA20_WK'
    ,'MA60_WK'
    ,'MA120_WK'
    ,'MA180_WK'
    ,'CDL2CROWS_WK'
    ,'CDL3BLACKCROWS_WK'
    ,'CDL3INSIDE_WK'
    ,'CDL3LINESTRIKE_WK'
    ,'CDL3OUTSIDE_WK'
    ,'CDL3STARSINSOUTH_WK'
    ,'CDL3WHITESOLDIERS_WK'
    ,'CDLABANDONEDBABY_WK'
    ,'CDLADVANCEBLOCK_WK'
    ,'CDLBELTHOLD_WK'
    ,'CDLBREAKAWAY_WK'
    ,'CDLCLOSINGMARUBOZU_WK'
    ,'CDLCONCEALBABYSWALL_WK'
    ,'CDLCOUNTERATTACK_WK'
    ,'CDLDARKCLOUDCOVER_WK'
    ,'CDLDOJI_WK'
    ,'CDLDOJISTAR_WK'
    ,'CDLDRAGONFLYDOJI_WK'
    ,'CDLENGULFING_WK'
    ,'CDLEVENINGDOJISTAR_WK'
    ,'CDLEVENINGSTAR_WK'
    ,'CDLGAPSIDESIDEWHITE_WK'
    ,'CDLGRAVESTONEDOJI_WK'
    ,'CDLHAMMER_WK'
    ,'CDLHANGINGMAN_WK'
    ,'CDLHARAMI_WK'
    ,'CDLHARAMICROSS_WK'
    ,'CDLHIGHWAVE_WK'
    ,'CDLHIKKAKE_WK'
    ,'CDLHIKKAKEMOD_WK'
    ,'CDLHOMINGPIGEON_WK'
    ,'CDLIDENTICAL3CROWS_WK'
    ,'CDLINNECK_WK'
    ,'CDLINVERTEDHAMMER_WK'
    ,'CDLKICKING_WK'
    ,'CDLKICKINGBYLENGTH_WK'
    ,'CDLLADDERBOTTOM_WK'
    ,'CDLLONGLEGGEDDOJI_WK'
    ,'CDLLONGLINE_WK'
    ,'CDLMARUBOZU_WK'
    ,'CDLMATCHINGLOW_WK'
    ,'CDLMATHOLD_WK'
    ,'CDLMORNINGDOJISTAR_WK'
    ,'CDLMORNINGSTAR_WK'
    ,'CDLONNECK_WK'
    ,'CDLPIERCING_WK'
    ,'CDLRICKSHAWMAN_WK'
    ,'CDLRISEFALL3METHODS_WK'
    ,'CDLSEPARATINGLINES_WK'
    ,'CDLSHOOTINGSTAR_WK'
    ,'CDLSHORTLINE_WK'
    ,'CDLSPINNINGTOP_WK'
    ,'CDLSTALLEDPATTERN_WK'
    ,'CDLSTICKSANDWICH_WK'
    ,'CDLTAKURI_WK'
    ,'CDLTASUKIGAP_WK'
    ,'CDLTHRUSTING_WK'
    ,'CDLTRISTAR_WK'
    ,'CDLUNIQUE3RIVER_WK'
    ,'CDLUPSIDEGAP2CROWS_WK'
    ,'CDLXSIDEGAP3METHODS_WK'
    ,'ALPHA_001'
    ,'ALPHA_002'
    ,'ALPHA_003'
    ,'ALPHA_004'
    ,'ALPHA_005'
    ,'ALPHA_006'
    ,'ALPHA_007'
    ,'ALPHA_008'
    ,'ALPHA_009'
    ,'ALPHA_010'
    ,'ALPHA_011'
    ,'ALPHA_012'
    ,'ALPHA_013'
    ,'ALPHA_014'
    ,'ALPHA_015'
    ,'ALPHA_016'
    ,'ALPHA_018'
    ,'ALPHA_019'
    ,'ALPHA_020'
    ,'ALPHA_021'
    ,'ALPHA_022'
    ,'ALPHA_023'
    ,'ALPHA_024'
    ,'ALPHA_025'
    ,'ALPHA_026'
    ,'ALPHA_028'
    ,'ALPHA_029'
    ,'ALPHA_031'
    ,'ALPHA_032'
    ,'ALPHA_033'
    ,'ALPHA_034'
    ,'ALPHA_035'
    ,'ALPHA_036'
    ,'ALPHA_037'
    ,'ALPHA_038'
    ,'ALPHA_039'
    ,'ALPHA_040'
    ,'ALPHA_041'
    ,'ALPHA_042'
    ,'ALPHA_043'
    ,'ALPHA_044'
    ,'ALPHA_045'
    ,'ALPHA_046'
    ,'ALPHA_047'
    ,'ALPHA_048'
    ,'ALPHA_049'
    ,'ALPHA_052'
    ,'ALPHA_053'
    ,'ALPHA_054'
    ,'ALPHA_056'
    ,'ALPHA_057'
    ,'ALPHA_058'
    ,'ALPHA_059'
    ,'ALPHA_060'
    ,'ALPHA_061'
    ,'ALPHA_062'
    ,'ALPHA_063'
    ,'ALPHA_064'
    ,'ALPHA_065'
    ,'ALPHA_066'
    ,'ALPHA_067'
    ,'ALPHA_068'
    ,'ALPHA_070'
    ,'ALPHA_071'
    ,'ALPHA_072'
    ,'ALPHA_074'
    ,'ALPHA_076'
    ,'ALPHA_077'
    ,'ALPHA_078'
    ,'ALPHA_079'
    ,'ALPHA_080'
    ,'ALPHA_081'
    ,'ALPHA_082'
    ,'ALPHA_083'
    ,'ALPHA_084'
    ,'ALPHA_085'
    ,'ALPHA_086'
    ,'ALPHA_087'
    ,'ALPHA_088'
    ,'ALPHA_089'
    ,'ALPHA_090'
    ,'ALPHA_091'
    ,'ALPHA_093'
    ,'ALPHA_094'
    ,'ALPHA_095'
    ,'ALPHA_096'
    ,'ALPHA_097'
    ,'ALPHA_098'
    ,'ALPHA_099'
    ,'ALPHA_100'
    ,'ALPHA_101'
    ,'ALPHA_102'
    ,'ALPHA_103'
    ,'ALPHA_104'
    ,'ALPHA_105'
    ,'ALPHA_106'
    ,'ALPHA_107'
    ,'ALPHA_108'
    ,'ALPHA_109'
    ,'ALPHA_111'
    ,'ALPHA_112'
    ,'ALPHA_114'
    ,'ALPHA_115'
    ,'ALPHA_117'
    ,'ALPHA_118'
    ,'ALPHA_119'
    ,'ALPHA_120'
    ,'ALPHA_122'
    ,'ALPHA_123'
    ,'ALPHA_124'
    ,'ALPHA_125'
    ,'ALPHA_126'
    ,'ALPHA_127'
    ,'ALPHA_128'
    ,'ALPHA_129'
    ,'ALPHA_130'
    ,'ALPHA_132'
    ,'ALPHA_133'
    ,'ALPHA_134'
    ,'ALPHA_135'
    ,'ALPHA_136'
    ,'ALPHA_137'
    ,'ALPHA_139'
    ,'ALPHA_141'
    ,'ALPHA_142'
    ,'ALPHA_145'
    ,'ALPHA_148'
    ,'ALPHA_150'
    ,'ALPHA_152'
    ,'ALPHA_153'
    ,'ALPHA_154'
    ,'ALPHA_155'
    ,'ALPHA_156'
    ,'ALPHA_157'
    ,'ALPHA_158'
    ,'ALPHA_159'
    ,'ALPHA_160'
    ,'ALPHA_161'
    ,'ALPHA_162'
    ,'ALPHA_163'
    ,'ALPHA_164'
    ,'ALPHA_167'
    ,'ALPHA_168'
    ,'ALPHA_169'
    ,'ALPHA_170'
    ,'ALPHA_172'
    ,'ALPHA_173'
    ,'ALPHA_174'
    ,'ALPHA_175'
    ,'ALPHA_177'
    ,'ALPHA_178'
    ,'ALPHA_179'
    ,'ALPHA_180'
    ,'ALPHA_184'
    ,'ALPHA_185'
    ,'ALPHA_186'
    ,'ALPHA_187'
    ,'ALPHA_188'
    ,'ALPHA_189'
    ,'ALPHA_191'
    ,'ALPHA001'
    ,'ALPHA002'
    ,'ALPHA003'
    ,'ALPHA004'
    ,'ALPHA005'
    ,'ALPHA006'
    ,'ALPHA007'
    ,'ALPHA008'
    ,'ALPHA009'
    ,'ALPHA010'
    ,'ALPHA011'
    ,'ALPHA012'
    ,'ALPHA013'
    ,'ALPHA014'
    ,'ALPHA015'
    ,'ALPHA016'
    ,'ALPHA017'
    ,'ALPHA018'
    ,'ALPHA019'
    ,'ALPHA020'
    ,'ALPHA021'
    ,'ALPHA022'
    ,'ALPHA023'
    ,'ALPHA024'
    ,'ALPHA025'
    ,'ALPHA026'
    ,'ALPHA027'
    ,'ALPHA028'
    ,'ALPHA029'
    ,'ALPHA030'
    ,'ALPHA031'
    ,'ALPHA032'
    ,'ALPHA033'
    ,'ALPHA034'
    ,'ALPHA035'
    ,'ALPHA036'
    ,'ALPHA037'
    ,'ALPHA038'
    ,'ALPHA039'
    ,'ALPHA040'
    ,'ALPHA041'
    ,'ALPHA042'
    ,'ALPHA043'
    ,'ALPHA044'
    ,'ALPHA045'
    ,'ALPHA046'
    ,'ALPHA047'
    ,'ALPHA049'
    ,'ALPHA050'
    ,'ALPHA051'
    ,'ALPHA052'
    ,'ALPHA053'
    ,'ALPHA054'
    ,'ALPHA055'
    ,'ALPHA057'
    ,'ALPHA060'
    ,'ALPHA061'
    ,'ALPHA062'
    ,'ALPHA064'
    ,'ALPHA065'
    ,'ALPHA066'
    ,'ALPHA068'
    ,'ALPHA071'
    ,'ALPHA072'
    ,'ALPHA073'
    ,'ALPHA074'
    ,'ALPHA075'
    ,'ALPHA077'
    ,'ALPHA078'
    ,'ALPHA081'
    ,'ALPHA083'
    ,'ALPHA085'
    ,'ALPHA086'
    ,'ALPHA088'
    ,'ALPHA092'
    ,'ALPHA094'
    ,'ALPHA095'
    ,'ALPHA096'
    ,'ALPHA098'
    ,'ALPHA099'
    ,'ALPHA101'
    ,'ALPHA001_HALF'
    ,'ALPHA002_HALF'
    ,'ALPHA003_HALF'
    ,'ALPHA004_HALF'
    ,'ALPHA005_HALF'
    ,'ALPHA006_HALF'
    ,'ALPHA007_HALF'
    ,'ALPHA008_HALF'
    ,'ALPHA009_HALF'
    ,'ALPHA010_HALF'
    ,'ALPHA011_HALF'
    ,'ALPHA012_HALF'
    ,'ALPHA013_HALF'
    ,'ALPHA014_HALF'
    ,'ALPHA015_HALF'
    ,'ALPHA016_HALF'
    ,'ALPHA017_HALF'
    ,'ALPHA018_HALF'
    ,'ALPHA019_HALF'
    ,'ALPHA020_HALF'
    ,'ALPHA021_HALF'
    ,'ALPHA022_HALF'
    ,'ALPHA023_HALF'
    ,'ALPHA024_HALF'
    ,'ALPHA025_HALF'
    ,'ALPHA026_HALF'
    ,'ALPHA027_HALF'
    ,'ALPHA028_HALF'
    ,'ALPHA029_HALF'
    ,'ALPHA030_HALF'
    ,'ALPHA031_HALF'
    ,'ALPHA032_HALF'
    ,'ALPHA033_HALF'
    ,'ALPHA034_HALF'
    ,'ALPHA035_HALF'
    ,'ALPHA036_HALF'
    ,'ALPHA037_HALF'
    ,'ALPHA038_HALF'
    ,'ALPHA039_HALF'
    ,'ALPHA040_HALF'
    ,'ALPHA041_HALF'
    ,'ALPHA042_HALF'
    ,'ALPHA043_HALF'
    ,'ALPHA044_HALF'
    ,'ALPHA045_HALF'
    ,'ALPHA046_HALF'
    ,'ALPHA047_HALF'
    ,'ALPHA049_HALF'
    ,'ALPHA050_HALF'
    ,'ALPHA051_HALF'
    ,'ALPHA052_HALF'
    ,'ALPHA053_HALF'
    ,'ALPHA054_HALF'
    ,'ALPHA055_HALF'
    ,'ALPHA057_HALF'
    ,'ALPHA060_HALF'
    ,'ALPHA061_HALF'
    ,'ALPHA062_HALF'
    ,'ALPHA064_HALF'
    ,'ALPHA065_HALF'
    ,'ALPHA066_HALF'
    ,'ALPHA068_HALF'
    ,'ALPHA071_HALF'
    ,'ALPHA072_HALF'
    ,'ALPHA073_HALF'
    ,'ALPHA074_HALF'
    ,'ALPHA075_HALF'
    ,'ALPHA077_HALF'
    ,'ALPHA078_HALF'
    ,'ALPHA081_HALF'
    ,'ALPHA083_HALF'
    ,'ALPHA085_HALF'
    ,'ALPHA086_HALF'
    ,'ALPHA088_HALF'
    ,'ALPHA092_HALF'
    ,'ALPHA094_HALF'
    ,'ALPHA095_HALF'
    ,'ALPHA096_HALF'
    ,'ALPHA098_HALF'
    ,'ALPHA099_HALF'
    ,'ALPHA101_HALF'
    ,'ALPHA_001_HALF'
    ,'ALPHA_002_HALF'
    ,'ALPHA_003_HALF'
    ,'ALPHA_004_HALF'
    ,'ALPHA_005_HALF'
    ,'ALPHA_006_HALF'
    ,'ALPHA_007_HALF'
    ,'ALPHA_008_HALF'
    ,'ALPHA_009_HALF'
    ,'ALPHA_010_HALF'
    ,'ALPHA_011_HALF'
    ,'ALPHA_012_HALF'
    ,'ALPHA_013_HALF'
    ,'ALPHA_014_HALF'
    ,'ALPHA_015_HALF'
    ,'ALPHA_016_HALF'
    ,'ALPHA_018_HALF'
    ,'ALPHA_019_HALF'
    ,'ALPHA_020_HALF'
    ,'ALPHA_021_HALF'
    ,'ALPHA_022_HALF'
    ,'ALPHA_023_HALF'
    ,'ALPHA_024_HALF'
    ,'ALPHA_025_HALF'
    ,'ALPHA_028_HALF'
    ,'ALPHA_029_HALF'
    ,'ALPHA_031_HALF'
    ,'ALPHA_032_HALF'
    ,'ALPHA_034_HALF'
    ,'ALPHA_035_HALF'
    ,'ALPHA_036_HALF'
    ,'ALPHA_037_HALF'
    ,'ALPHA_038_HALF'
    ,'ALPHA_040_HALF'
    ,'ALPHA_041_HALF'
    ,'ALPHA_042_HALF'
    ,'ALPHA_043_HALF'
    ,'ALPHA_044_HALF'
    ,'ALPHA_046_HALF'
    ,'ALPHA_047_HALF'
    ,'ALPHA_048_HALF'
    ,'ALPHA_049_HALF'
    ,'ALPHA_052_HALF'
    ,'ALPHA_053_HALF'
    ,'ALPHA_054_HALF'
    ,'ALPHA_056_HALF'
    ,'ALPHA_057_HALF'
    ,'ALPHA_058_HALF'
    ,'ALPHA_059_HALF'
    ,'ALPHA_060_HALF'
    ,'ALPHA_061_HALF'
    ,'ALPHA_062_HALF'
    ,'ALPHA_063_HALF'
    ,'ALPHA_064_HALF'
    ,'ALPHA_065_HALF'
    ,'ALPHA_066_HALF'
    ,'ALPHA_067_HALF'
    ,'ALPHA_068_HALF'
    ,'ALPHA_070_HALF'
    ,'ALPHA_071_HALF'
    ,'ALPHA_072_HALF'
    ,'ALPHA_074_HALF'
    ,'ALPHA_076_HALF'
    ,'ALPHA_077_HALF'
    ,'ALPHA_078_HALF'
    ,'ALPHA_079_HALF'
    ,'ALPHA_080_HALF'
    ,'ALPHA_081_HALF'
    ,'ALPHA_082_HALF'
    ,'ALPHA_083_HALF'
    ,'ALPHA_084_HALF'
    ,'ALPHA_085_HALF'
    ,'ALPHA_086_HALF'
    ,'ALPHA_087_HALF'
    ,'ALPHA_088_HALF'
    ,'ALPHA_089_HALF'
    ,'ALPHA_090_HALF'
    ,'ALPHA_091_HALF'
    ,'ALPHA_093_HALF'
    ,'ALPHA_094_HALF'
    ,'ALPHA_095_HALF'
    ,'ALPHA_096_HALF'
    ,'ALPHA_097_HALF'
    ,'ALPHA_098_HALF'
    ,'ALPHA_099_HALF'
    ,'ALPHA_100_HALF'
    ,'ALPHA_101_HALF'
    ,'ALPHA_102_HALF'
    ,'ALPHA_103_HALF'
    ,'ALPHA_104_HALF'
    ,'ALPHA_105_HALF'
    ,'ALPHA_106_HALF'
    ,'ALPHA_107_HALF'
    ,'ALPHA_109_HALF'
    ,'ALPHA_111_HALF'
    ,'ALPHA_112_HALF'
    ,'ALPHA_114_HALF'
    ,'ALPHA_115_HALF'
    ,'ALPHA_117_HALF'
    ,'ALPHA_118_HALF'
    ,'ALPHA_119_HALF'
    ,'ALPHA_120_HALF'
    ,'ALPHA_122_HALF'
    ,'ALPHA_123_HALF'
    ,'ALPHA_124_HALF'
    ,'ALPHA_125_HALF'
    ,'ALPHA_126_HALF'
    ,'ALPHA_129_HALF'
    ,'ALPHA_130_HALF'
    ,'ALPHA_132_HALF'
    ,'ALPHA_133_HALF'
    ,'ALPHA_134_HALF'
    ,'ALPHA_135_HALF'
    ,'ALPHA_136_HALF'
    ,'ALPHA_139_HALF'
    ,'ALPHA_141_HALF'
    ,'ALPHA_142_HALF'
    ,'ALPHA_145_HALF'
    ,'ALPHA_148_HALF'
    ,'ALPHA_150_HALF'
    ,'ALPHA_152_HALF'
    ,'ALPHA_153_HALF'
    ,'ALPHA_154_HALF'
    ,'ALPHA_155_HALF'
    ,'ALPHA_156_HALF'
    ,'ALPHA_157_HALF'
    ,'ALPHA_158_HALF'
    ,'ALPHA_159_HALF'
    ,'ALPHA_160_HALF'
    ,'ALPHA_161_HALF'
    ,'ALPHA_163_HALF'
    ,'ALPHA_164_HALF'
    ,'ALPHA_167_HALF'
    ,'ALPHA_168_HALF'
    ,'ALPHA_169_HALF'
    ,'ALPHA_170_HALF'
    ,'ALPHA_172_HALF'
    ,'ALPHA_173_HALF'
    ,'ALPHA_174_HALF'
    ,'ALPHA_175_HALF'
    ,'ALPHA_177_HALF'
    ,'ALPHA_178_HALF'
    ,'ALPHA_179_HALF'
    ,'ALPHA_180_HALF'
    ,'ALPHA_185_HALF'
    ,'ALPHA_186_HALF'
    ,'ALPHA_187_HALF'
    ,'ALPHA_188_HALF'
    ,'ALPHA_189_HALF'
    ,'ALPHA_191_HALF'
    ,'PE_10PCT'
    ,'PE_10VAL'
    ,'PEEGL_10PCT'
    ,'PEEGL_10VAL'
    ,'PB_10PCT'
    ,'PB_10VAL'
    ,'PS_10PCT'
    ,'PS_10VAL'
    ,'PE_20PCT'
    ,'PE_20VAL'
    ,'PEEGL_20PCT'
    ,'PEEGL_20VAL'
    ,'PB_20PCT'
    ,'PB_20VAL'
    ,'PS_20PCT'
    ,'PS_20VAL'
    ,'PE_30PCT'
    ,'PE_30VAL'
    ,'PE_30DN'
    ,'PE_30UP'
    ,'PEEGL_30PCT'
    ,'PEEGL_30VAL'
    ,'PEEGL_30DN'
    ,'PEEGL_30UP'
    ,'PB_30PCT'
    ,'PB_30VAL'
    ,'PB_30DN'
    ,'PB_30UP'
    ,'PS_30PCT'
    ,'PS_30VAL'
    ,'PS_30DN'
    ,'PS_30UP'
    ,'PE_60PCT'
    ,'PE_60VAL'
    ,'PE_60DN'
    ,'PE_60UP'
    ,'PEEGL_60PCT'
    ,'PEEGL_60VAL'
    ,'PEEGL_60DN'
    ,'PEEGL_60UP'
    ,'PB_60PCT'
    ,'PB_60VAL'
    ,'PB_60DN'
    ,'PB_60UP'
    ,'PS_60PCT'
    ,'PS_60VAL'
    ,'PS_60DN'
    ,'PS_60UP'
    ,'PE_90PCT'
    ,'PE_90VAL'
    ,'PE_90DN'
    ,'PE_90UP'
    ,'PEEGL_90PCT'
    ,'PEEGL_90VAL'
    ,'PEEGL_90DN'
    ,'PEEGL_90UP'
    ,'PB_90PCT'
    ,'PB_90VAL'
    ,'PB_90DN'
    ,'PB_90UP'
    ,'RNG_HALF'
    ,'RNG_L_HALF'
    ,'RNG_5_HALF'
    ,'RNG_10_HALF'
    ,'RNG_20_HALF'
    ,'RNG_30_HALF'
    ,'RNG_60_HALF'
    ,'RNG_90_HALF'
    ,'LAG_HALF'
    ,'LAG2_HALF'
    ,'LAG3_HALF'
    ,'LAG5_HALF'
    ,'LAG10_HALF'
    ,'LAG20_HALF'
    ,'LAG30_HALF'
    ,'LAG60_HALF'
    ,'LAG90_HALF'
    ,'AVG5_HALF'
    ,'AVG10_HALF'
    ,'AVG20_HALF'
    ,'AVG30_HALF'
    ,'AVG60_HALF'
    ,'AVG90_HALF'
    ,'AMT_L_HALF'
    ,'AMT_5_HALF'
    ,'AMT_10_HALF'
    ,'AMT_20_HALF'
    ,'AMT_30_HALF'
    ,'AMT_60_HALF'
    ,'AMT_90_HALF'
    ,'MAMT_5_HALF'
    ,'MAMT_10_HALF'
    ,'MAMT_20_HALF'
    ,'MAMT_30_HALF'
    ,'MAMT_60_HALF'
    ,'MAMT_90_HALF'
    ,'AVG5_C_HALF'
    ,'AVG10_C_HALF'
    ,'AVG20_C_HALF'
    ,'AVG30_C_HALF'
    ,'AVG60_C_HALF'
    ,'AVG90_C_HALF']

data_set = ['TOTAL_MARKET'
    ,'TRA_RATE'
    ,'DAYS'
    ,'AVG5'
    ,'AVG10'
    ,'AVG20'
    ,'AVG30'
    ,'AVG60'
    ,'LAG'
    ,'LAG5'
    ,'LAG10'
    ,'LAG20'
    ,'LAG30'
    ,'LAG60'
    ,'AVG5_TOR'
    ,'AVG20_TOR'
    ,'AVG30_TOR'
    ,'AVG60_TOR'
    ,'GROSSMARGIN'
    ,'NETPROFIT_INRATE'
    ,'OPERATINGRINRATE'
    ,'NETCASHOPERATINRATE'
    ,'PB'
    ,'PBG'
    ,'PC'
    ,'PE_TTM'
    ,'PEEGL_TTM'
    ,'PEG'
    ,'PM'
    ,'PS'
    ,'PSG'
    ,'PT'
    ,'PE_RATE'
    ,'PEEGL_RATE'
    ,'PB_RATE'
    ,'ROE_RATE'
    ,'ROE_RATET'
    ,'ROA_RATE'
    ,'ROA_RATET'
    ,'GROSS_RATE'
    ,'RNG'
    ,'RNG_L'
    ,'RNG_5'
    ,'RNG_10'
    ,'RNG_20'
    ,'RNG_30'
    ,'RNG_60'
    ,'RNG_90'
    ,'AMT_L'
    ,'AMT_5'
    ,'AMT_10'
    ,'AMT_20'
    ,'AMT_30'
    ,'AMT_60'
    ,'AMT_90'
    ,'MAMT_5'
    ,'MAMT_10'
    ,'MAMT_20'
    ,'MAMT_30'
    ,'MAMT_60'
    ,'MAMT_90'
    ,'AVG5_RNG'
    ,'AVG10_RNG'
    ,'AVG20_RNG'
    ,'AVG30_RNG'
    ,'AVG60_RNG'
    ,'ROA'
    ,'ROE'
    ,'AVG5_CR'
    ,'AVG10_CR'
    ,'AVG20_CR'
    ,'AVG30_CR'
    ,'AVG60_CR'
    ,'AVG5_TR'
    ,'AVG10_TR'
    ,'AVG20_TR'
    ,'AVG30_TR'
    ,'AVG60_TR'
    ,'TOTALPROFITINRATE'
    ,'VR'
    ,'VRSI'
    ,'VRSI_C'
    ,'VSTD'
    ,'BOLL'
    ,'UB'
    ,'LB'
    ,'WIDTH'
    ,'WR'
    ,'MR'
    ,'SR'
    ,'WS'
    ,'MS'
    ,'SS'
    ,'MIKE_WRSC'
    ,'MIKE_WRJC'
    ,'MIKE_WSSC'
    ,'MIKE_WSJC'
    ,'MIKE_TR'
    ,'MIKE_BOLL'
    ,'ASI'
    ,'ASIT'
    ,'OBV'
    ,'OBV_C'
    ,'PVT'
    ,'VPT'
    ,'MAVPT'
    ,'VPT_CROSS1'
    ,'VPT_CROSS2'
    ,'VPT_CROSS3'
    ,'VPT_CROSS4'
    ,'KDJ_K'
    ,'KDJ_D'
    ,'KDJ_J'
    ,'KDJ_CROSS1'
    ,'KDJ_CROSS2'
    ,'WR1'
    ,'WR2'
    ,'WR_CROSS1'
    ,'WR_CROSS2'
    ,'ROC'
    ,'ROCMA'
    ,'RSI1'
    ,'RSI2'
    ,'RSI3'
    ,'RSI1_C'
    ,'RSI2_C'
    ,'RSI3_C'
    ,'RSI_CROSS1'
    ,'RSI_CROSS2'
    ,'CCI'
    ,'CCI_CROSS1'
    ,'CCI_CROSS2'
    ,'CCI_CROSS3'
    ,'CCI_CROSS4'
    ,'BIAS1'
    ,'BIAS2'
    ,'BIAS3'
    ,'BIAS_CROSS1'
    ,'BIAS_CROSS2'
    ,'OSC'
    ,'MAOSC'
    ,'OSC_CROSS1'
    ,'OSC_CROSS2'
    ,'OSC_CROSS3'
    ,'OSC_CROSS4'
    ,'ADTM'
    ,'MAADTM'
    ,'ADTM_CROSS1'
    ,'ADTM_CROSS2'
    ,'DIF'
    ,'DEA'
    ,'MACD'
    ,'CROSS_JC'
    ,'CROSS_SC'
    ,'MACD_TR'
    ,'DI1'
    ,'DI2'
    ,'ADX'
    ,'ADXR'
    ,'ADX_C'
    ,'DI_M'
    ,'DI_CROSS1'
    ,'DI_CROSS2'
    ,'ADX_CROSS1'
    ,'ADX_CROSS2'
    ,'DDD'
    ,'AMA'
    ,'DMA_CROSS1'
    ,'DMA_CROSS2'
    ,'MTM'
    ,'MTMMA'
    ,'MTM_CROSS1'
    ,'MTM_CROSS2'
    ,'MTM_CROSS3'
    ,'MTM_CROSS4'
    ,'MA1'
    ,'MA2'
    ,'MA3'
    ,'MA4'
    ,'CHO'
    ,'MACHO'
    ,'CHO_CROSS1'
    ,'CHO_CROSS2'
    ,'BBI'
    ,'BBI_CROSS1'
    ,'BBI_CROSS2'
    ,'MFI'
    ,'MFI_C'
    ,'TR'
    ,'ATR'
    ,'ATRR'
    ,'RSV'
    ,'SKDJ_K'
    ,'SKDJ_D'
    ,'SKDJ_CROSS1'
    ,'SKDJ_CROSS2'
    ,'DDI'
    ,'ADDI'
    ,'AD'
    ,'DDI_C'
    ,'AD_C'
    ,'ADDI_C'
    ,'SHA_LOW'
    ,'SHA_UP'
    ,'BODY'
    ,'BODY_ABS'
    ,'PRICE_PCG'
    ,'MA5'
    ,'MA10'
    ,'MA20'
    ,'MA60'
    ,'MA120'
    ,'MA180'
    ,'CDL2CROWS'
    ,'CDL3BLACKCROWS'
    ,'CDL3INSIDE'
    ,'CDL3LINESTRIKE'
    ,'CDL3OUTSIDE'
    ,'CDL3STARSINSOUTH'
    ,'CDL3WHITESOLDIERS'
    ,'CDLABANDONEDBABY'
    ,'CDLADVANCEBLOCK'
    ,'CDLBELTHOLD'
    ,'CDLBREAKAWAY'
    ,'CDLCLOSINGMARUBOZU'
    ,'CDLCONCEALBABYSWALL'
    ,'CDLCOUNTERATTACK'
    ,'CDLDARKCLOUDCOVER'
    ,'CDLDOJI'
    ,'CDLDOJISTAR'
    ,'CDLDRAGONFLYDOJI'
    ,'CDLENGULFING'
    ,'CDLEVENINGDOJISTAR'
    ,'CDLEVENINGSTAR'
    ,'CDLGAPSIDESIDEWHITE'
    ,'CDLGRAVESTONEDOJI'
    ,'CDLHAMMER'
    ,'CDLHANGINGMAN'
    ,'CDLHARAMI'
    ,'CDLHARAMICROSS'
    ,'CDLHIGHWAVE'
    ,'CDLHIKKAKE'
    ,'CDLHIKKAKEMOD'
    ,'CDLHOMINGPIGEON'
    ,'CDLIDENTICAL3CROWS'
    ,'CDLINNECK'
    ,'CDLINVERTEDHAMMER'
    ,'CDLKICKING'
    ,'CDLKICKINGBYLENGTH'
    ,'CDLLADDERBOTTOM'
    ,'CDLLONGLEGGEDDOJI'
    ,'CDLLONGLINE'
    ,'CDLMARUBOZU'
    ,'CDLMATCHINGLOW'
    ,'CDLMATHOLD'
    ,'CDLMORNINGDOJISTAR'
    ,'CDLMORNINGSTAR'
    ,'CDLONNECK'
    ,'CDLPIERCING'
    ,'CDLRICKSHAWMAN'
    ,'CDLRISEFALL3METHODS'
    ,'CDLSEPARATINGLINES'
    ,'CDLSHOOTINGSTAR'
    ,'CDLSHORTLINE'
    ,'CDLSPINNINGTOP'
    ,'CDLSTALLEDPATTERN'
    ,'CDLSTICKSANDWICH'
    ,'CDLTAKURI'
    ,'CDLTASUKIGAP'
    ,'CDLTHRUSTING'
    ,'CDLTRISTAR'
    ,'CDLUNIQUE3RIVER'
    ,'CDLUPSIDEGAP2CROWS'
    ,'CDLXSIDEGAP3METHODS'
    ,'VR_WK'
    ,'VRSI_WK'
    ,'VRSI_C_WK'
    ,'VSTD_WK'
    ,'BOLL_WK'
    ,'UB_WK'
    ,'LB_WK'
    ,'WIDTH_WK'
    ,'WR_WK'
    ,'MR_WK'
    ,'SR_WK'
    ,'WS_WK'
    ,'MS_WK'
    ,'SS_WK'
    ,'MIKE_WRSC_WK'
    ,'MIKE_WRJC_WK'
    ,'MIKE_WSSC_WK'
    ,'MIKE_WSJC_WK'
    ,'MIKE_TR_WK'
    ,'MIKE_BOLL_WK'
    ,'ASI_WK'
    ,'ASIT_WK'
    ,'OBV_WK'
    ,'OBV_C_WK'
    ,'PVT_WK'
    ,'VPT_WK'
    ,'MAVPT_WK'
    ,'VPT_CROSS1_WK'
    ,'VPT_CROSS2_WK'
    ,'VPT_CROSS3_WK'
    ,'VPT_CROSS4_WK'
    ,'KDJ_K_WK'
    ,'KDJ_D_WK'
    ,'KDJ_J_WK'
    ,'KDJ_CROSS1_WK'
    ,'KDJ_CROSS2_WK'
    ,'WR1_WK'
    ,'WR2_WK'
    ,'WR_CROSS1_WK'
    ,'WR_CROSS2_WK'
    ,'ROC_WK'
    ,'ROCMA_WK'
    ,'RSI1_WK'
    ,'RSI2_WK'
    ,'RSI3_WK'
    ,'RSI1_C_WK'
    ,'RSI2_C_WK'
    ,'RSI3_C_WK'
    ,'RSI_CROSS1_WK'
    ,'RSI_CROSS2_WK'
    ,'CCI_WK'
    ,'CCI_CROSS1_WK'
    ,'CCI_CROSS2_WK'
    ,'CCI_CROSS3_WK'
    ,'CCI_CROSS4_WK'
    ,'BIAS1_WK'
    ,'BIAS2_WK'
    ,'BIAS3_WK'
    ,'BIAS_CROSS1_WK'
    ,'BIAS_CROSS2_WK'
    ,'OSC_WK'
    ,'MAOSC_WK'
    ,'OSC_CROSS1_WK'
    ,'OSC_CROSS2_WK'
    ,'OSC_CROSS3_WK'
    ,'OSC_CROSS4_WK'
    ,'ADTM_WK'
    ,'MAADTM_WK'
    ,'ADTM_CROSS1_WK'
    ,'ADTM_CROSS2_WK'
    ,'DIF_WK'
    ,'DEA_WK'
    ,'MACD_WK'
    ,'CROSS_JC_WK'
    ,'CROSS_SC_WK'
    ,'MACD_TR_WK'
    ,'DI1_WK'
    ,'DI2_WK'
    ,'ADX_WK'
    ,'ADXR_WK'
    ,'ADX_C_WK'
    ,'DI_M_WK'
    ,'DI_CROSS1_WK'
    ,'DI_CROSS2_WK'
    ,'ADX_CROSS1_WK'
    ,'ADX_CROSS2_WK'
    ,'DDD_WK'
    ,'AMA_WK'
    ,'DMA_CROSS1_WK'
    ,'DMA_CROSS2_WK'
    ,'MTM_WK'
    ,'MTMMA_WK'
    ,'MTM_CROSS1_WK'
    ,'MTM_CROSS2_WK'
    ,'MTM_CROSS3_WK'
    ,'MTM_CROSS4_WK'
    ,'MA1_WK'
    ,'MA2_WK'
    ,'MA3_WK'
    ,'MA4_WK'
    ,'CHO_WK'
    ,'MACHO_WK'
    ,'CHO_CROSS1_WK'
    ,'CHO_CROSS2_WK'
    ,'BBI_WK'
    ,'BBI_CROSS1_WK'
    ,'BBI_CROSS2_WK'
    ,'MFI_WK'
    ,'MFI_C_WK'
    ,'TR_WK'
    ,'ATR_WK'
    ,'ATRR_WK'
    ,'RSV_WK'
    ,'SKDJ_K_WK'
    ,'SKDJ_D_WK'
    ,'SKDJ_CROSS1_WK'
    ,'SKDJ_CROSS2_WK'
    ,'DDI_WK'
    ,'ADDI_WK'
    ,'AD_WK'
    ,'DDI_C_WK'
    ,'AD_C_WK'
    ,'ADDI_C_WK'
    ,'SHA_LOW_WK'
    ,'SHA_UP_WK'
    ,'BODY_WK'
    ,'BODY_ABS_WK'
    ,'PRICE_PCG_WK'
    ,'MA5_WK'
    ,'MA10_WK'
    ,'MA20_WK'
    ,'MA60_WK'
    ,'MA120_WK'
    ,'MA180_WK'
    ,'CDL2CROWS_WK'
    ,'CDL3BLACKCROWS_WK'
    ,'CDL3INSIDE_WK'
    ,'CDL3LINESTRIKE_WK'
    ,'CDL3OUTSIDE_WK'
    ,'CDL3STARSINSOUTH_WK'
    ,'CDL3WHITESOLDIERS_WK'
    ,'CDLABANDONEDBABY_WK'
    ,'CDLADVANCEBLOCK_WK'
    ,'CDLBELTHOLD_WK'
    ,'CDLBREAKAWAY_WK'
    ,'CDLCLOSINGMARUBOZU_WK'
    ,'CDLCONCEALBABYSWALL_WK'
    ,'CDLCOUNTERATTACK_WK'
    ,'CDLDARKCLOUDCOVER_WK'
    ,'CDLDOJI_WK'
    ,'CDLDOJISTAR_WK'
    ,'CDLDRAGONFLYDOJI_WK'
    ,'CDLENGULFING_WK'
    ,'CDLEVENINGDOJISTAR_WK'
    ,'CDLEVENINGSTAR_WK'
    ,'CDLGAPSIDESIDEWHITE_WK'
    ,'CDLGRAVESTONEDOJI_WK'
    ,'CDLHAMMER_WK'
    ,'CDLHANGINGMAN_WK'
    ,'CDLHARAMI_WK'
    ,'CDLHARAMICROSS_WK'
    ,'CDLHIGHWAVE_WK'
    ,'CDLHIKKAKE_WK'
    ,'CDLHIKKAKEMOD_WK'
    ,'CDLHOMINGPIGEON_WK'
    ,'CDLIDENTICAL3CROWS_WK'
    ,'CDLINNECK_WK'
    ,'CDLINVERTEDHAMMER_WK'
    ,'CDLKICKING_WK'
    ,'CDLKICKINGBYLENGTH_WK'
    ,'CDLLADDERBOTTOM_WK'
    ,'CDLLONGLEGGEDDOJI_WK'
    ,'CDLLONGLINE_WK'
    ,'CDLMARUBOZU_WK'
    ,'CDLMATCHINGLOW_WK'
    ,'CDLMATHOLD_WK'
    ,'CDLMORNINGDOJISTAR_WK'
    ,'CDLMORNINGSTAR_WK'
    ,'CDLONNECK_WK'
    ,'CDLPIERCING_WK'
    ,'CDLRICKSHAWMAN_WK'
    ,'CDLRISEFALL3METHODS_WK'
    ,'CDLSEPARATINGLINES_WK'
    ,'CDLSHOOTINGSTAR_WK'
    ,'CDLSHORTLINE_WK'
    ,'CDLSPINNINGTOP_WK'
    ,'CDLSTALLEDPATTERN_WK'
    ,'CDLSTICKSANDWICH_WK'
    ,'CDLTAKURI_WK'
    ,'CDLTASUKIGAP_WK'
    ,'CDLTHRUSTING_WK'
    ,'CDLTRISTAR_WK'
    ,'CDLUNIQUE3RIVER_WK'
    ,'CDLUPSIDEGAP2CROWS_WK'
    ,'CDLXSIDEGAP3METHODS_WK'
    ,'ALPHA_001'
    ,'ALPHA_002'
    ,'ALPHA_003'
    ,'ALPHA_004'
    ,'ALPHA_005'
    ,'ALPHA_006'
    ,'ALPHA_007'
    ,'ALPHA_008'
    ,'ALPHA_009'
    ,'ALPHA_010'
    ,'ALPHA_011'
    ,'ALPHA_012'
    ,'ALPHA_013'
    ,'ALPHA_014'
    ,'ALPHA_015'
    ,'ALPHA_016'
    ,'ALPHA_018'
    ,'ALPHA_019'
    ,'ALPHA_020'
    ,'ALPHA_021'
    ,'ALPHA_022'
    ,'ALPHA_023'
    ,'ALPHA_024'
    ,'ALPHA_025'
    ,'ALPHA_026'
    ,'ALPHA_028'
    ,'ALPHA_029'
    ,'ALPHA_031'
    ,'ALPHA_032'
    ,'ALPHA_033'
    ,'ALPHA_034'
    ,'ALPHA_035'
    ,'ALPHA_036'
    ,'ALPHA_037'
    ,'ALPHA_038'
    ,'ALPHA_039'
    ,'ALPHA_040'
    ,'ALPHA_041'
    ,'ALPHA_042'
    ,'ALPHA_043'
    ,'ALPHA_044'
    ,'ALPHA_045'
    ,'ALPHA_046'
    ,'ALPHA_047'
    ,'ALPHA_048'
    ,'ALPHA_049'
    ,'ALPHA_052'
    ,'ALPHA_053'
    ,'ALPHA_054'
    ,'ALPHA_056'
    ,'ALPHA_057'
    ,'ALPHA_058'
    ,'ALPHA_059'
    ,'ALPHA_060'
    ,'ALPHA_061'
    ,'ALPHA_062'
    ,'ALPHA_063'
    ,'ALPHA_064'
    ,'ALPHA_065'
    ,'ALPHA_066'
    ,'ALPHA_067'
    ,'ALPHA_068'
    ,'ALPHA_070'
    ,'ALPHA_071'
    ,'ALPHA_072'
    ,'ALPHA_074'
    ,'ALPHA_076'
    ,'ALPHA_077'
    ,'ALPHA_078'
    ,'ALPHA_079'
    ,'ALPHA_080'
    ,'ALPHA_081'
    ,'ALPHA_082'
    ,'ALPHA_083'
    ,'ALPHA_084'
    ,'ALPHA_085'
    ,'ALPHA_086'
    ,'ALPHA_087'
    ,'ALPHA_088'
    ,'ALPHA_089'
    ,'ALPHA_090'
    ,'ALPHA_091'
    ,'ALPHA_093'
    ,'ALPHA_094'
    ,'ALPHA_095'
    ,'ALPHA_096'
    ,'ALPHA_097'
    ,'ALPHA_098'
    ,'ALPHA_099'
    ,'ALPHA_100'
    ,'ALPHA_101'
    ,'ALPHA_102'
    ,'ALPHA_103'
    ,'ALPHA_104'
    ,'ALPHA_105'
    ,'ALPHA_106'
    ,'ALPHA_107'
    ,'ALPHA_108'
    ,'ALPHA_109'
    ,'ALPHA_111'
    ,'ALPHA_112'
    ,'ALPHA_114'
    ,'ALPHA_115'
    ,'ALPHA_117'
    ,'ALPHA_118'
    ,'ALPHA_119'
    ,'ALPHA_120'
    ,'ALPHA_122'
    ,'ALPHA_123'
    ,'ALPHA_124'
    ,'ALPHA_125'
    ,'ALPHA_126'
    ,'ALPHA_127'
    ,'ALPHA_128'
    ,'ALPHA_129'
    ,'ALPHA_130'
    ,'ALPHA_132'
    ,'ALPHA_133'
    ,'ALPHA_134'
    ,'ALPHA_135'
    ,'ALPHA_136'
    ,'ALPHA_137'
    ,'ALPHA_139'
    ,'ALPHA_141'
    ,'ALPHA_142'
    ,'ALPHA_145'
    ,'ALPHA_148'
    ,'ALPHA_150'
    ,'ALPHA_152'
    ,'ALPHA_153'
    ,'ALPHA_154'
    ,'ALPHA_155'
    ,'ALPHA_156'
    ,'ALPHA_157'
    ,'ALPHA_158'
    ,'ALPHA_159'
    ,'ALPHA_160'
    ,'ALPHA_161'
    ,'ALPHA_162'
    ,'ALPHA_163'
    ,'ALPHA_164'
    ,'ALPHA_167'
    ,'ALPHA_168'
    ,'ALPHA_169'
    ,'ALPHA_170'
    ,'ALPHA_172'
    ,'ALPHA_173'
    ,'ALPHA_174'
    ,'ALPHA_175'
    ,'ALPHA_177'
    ,'ALPHA_178'
    ,'ALPHA_179'
    ,'ALPHA_180'
    ,'ALPHA_184'
    ,'ALPHA_185'
    ,'ALPHA_186'
    ,'ALPHA_187'
    ,'ALPHA_188'
    ,'ALPHA_189'
    ,'ALPHA_191'
    ,'ALPHA001'
    ,'ALPHA002'
    ,'ALPHA003'
    ,'ALPHA004'
    ,'ALPHA005'
    ,'ALPHA006'
    ,'ALPHA007'
    ,'ALPHA008'
    ,'ALPHA009'
    ,'ALPHA010'
    ,'ALPHA011'
    ,'ALPHA012'
    ,'ALPHA013'
    ,'ALPHA014'
    ,'ALPHA015'
    ,'ALPHA016'
    ,'ALPHA017'
    ,'ALPHA018'
    ,'ALPHA019'
    ,'ALPHA020'
    ,'ALPHA021'
    ,'ALPHA022'
    ,'ALPHA023'
    ,'ALPHA024'
    ,'ALPHA025'
    ,'ALPHA026'
    ,'ALPHA027'
    ,'ALPHA028'
    ,'ALPHA029'
    ,'ALPHA030'
    ,'ALPHA031'
    ,'ALPHA032'
    ,'ALPHA033'
    ,'ALPHA034'
    ,'ALPHA035'
    ,'ALPHA036'
    ,'ALPHA037'
    ,'ALPHA038'
    ,'ALPHA039'
    ,'ALPHA040'
    ,'ALPHA041'
    ,'ALPHA042'
    ,'ALPHA043'
    ,'ALPHA044'
    ,'ALPHA045'
    ,'ALPHA046'
    ,'ALPHA047'
    ,'ALPHA049'
    ,'ALPHA050'
    ,'ALPHA051'
    ,'ALPHA052'
    ,'ALPHA053'
    ,'ALPHA054'
    ,'ALPHA055'
    ,'ALPHA057'
    ,'ALPHA060'
    ,'ALPHA061'
    ,'ALPHA062'
    ,'ALPHA064'
    ,'ALPHA065'
    ,'ALPHA066'
    ,'ALPHA068'
    ,'ALPHA071'
    ,'ALPHA072'
    ,'ALPHA073'
    ,'ALPHA074'
    ,'ALPHA075'
    ,'ALPHA077'
    ,'ALPHA078'
    ,'ALPHA081'
    ,'ALPHA083'
    ,'ALPHA085'
    ,'ALPHA086'
    ,'ALPHA088'
    ,'ALPHA092'
    ,'ALPHA094'
    ,'ALPHA095'
    ,'ALPHA096'
    ,'ALPHA098'
    ,'ALPHA099'
    ,'ALPHA101'
    ,'PE_10PCT'
    ,'PE_10VAL'
    ,'PEEGL_10PCT'
    ,'PEEGL_10VAL'
    ,'PB_10PCT'
    ,'PB_10VAL'
    ,'PS_10PCT'
    ,'PS_10VAL'
    ,'PE_20PCT'
    ,'PE_20VAL'
    ,'PEEGL_20PCT'
    ,'PEEGL_20VAL'
    ,'PB_20PCT'
    ,'PB_20VAL'
    ,'PS_20PCT'
    ,'PS_20VAL'
    ,'PE_30PCT'
    ,'PE_30VAL'
    ,'PE_30DN'
    ,'PE_30UP'
    ,'PEEGL_30PCT'
    ,'PEEGL_30VAL'
    ,'PEEGL_30DN'
    ,'PEEGL_30UP'
    ,'PB_30PCT'
    ,'PB_30VAL'
    ,'PB_30DN'
    ,'PB_30UP'
    ,'PS_30PCT'
    ,'PS_30VAL'
    ,'PS_30DN'
    ,'PS_30UP'
    ,'PE_60PCT'
    ,'PE_60VAL'
    ,'PE_60DN'
    ,'PE_60UP'
    ,'PEEGL_60PCT'
    ,'PEEGL_60VAL'
    ,'PEEGL_60DN'
    ,'PEEGL_60UP'
    ,'PB_60PCT'
    ,'PB_60VAL'
    ,'PB_60DN'
    ,'PB_60UP'
    ,'PS_60PCT'
    ,'PS_60VAL'
    ,'PS_60DN'
    ,'PS_60UP'
    ,'PE_90PCT'
    ,'PE_90VAL'
    ,'PE_90DN'
    ,'PE_90UP'
    ,'PEEGL_90PCT'
    ,'PEEGL_90VAL'
    ,'PEEGL_90DN'
    ,'PEEGL_90UP'
    ,'PB_90PCT'
    ,'PB_90VAL'
    ,'PB_90DN'
    ,'PB_90UP']
