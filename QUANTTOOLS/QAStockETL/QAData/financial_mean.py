# coding:utf-8

financial_dict = {

    # 1.每股指标
    '001基本每股收益' : 'EPS',
    '002扣除非经常性损益每股收益' : 'deductEPS',
    '003每股未分配利润' : 'undistributedProfitPerShare',
    '004每股净资产' : 'netAssetsPerShare',
    '005每股资本公积金' : 'capitalReservePerShare',
    '006净资产收益率' : 'ROE',
    '007每股经营现金流量' : 'operatingCashFlowPerShare',
    # 2. 资产负债表 BALANCE SHEET
    # 2.1 资产
    # 2.1.1 流动资产
    '008货币资金' : 'moneyFunds',
    '009交易性金融资产' : 'tradingFinancialAssets',
    '010应收票据' : 'billsReceivables',
    '011应收账款' : 'accountsReceivables',
    '012预付款项' : 'prepayments',
    '013其他应收款' : 'otherReceivables',
    '014应收关联公司款' : 'interCompanyReceivables',
    '015应收利息' : 'interestReceivables',
    '016应收股利' : 'dividendsReceivables',
    '017存货' : 'inventory',
    '018其中：消耗性生物资产' : 'expendableBiologicalAssets',
    '019一年内到期的非流动资产' : 'noncurrAssetsDueOneYear',
    '020其他流动资产' : 'otherLiquidAssets',
    '021流动资产合计' : 'totalLiquidAssets',
    # 2.1.2 非流动资产
    '022可供出售金融资产' : 'availableForSaleSecurities',
    '023持有至到期投资' : 'heldToMaturityInvestments',
    '024长期应收款' : 'longTermReceivables',
    '025长期股权投资' : 'longTermEquityInvestment',
    '026投资性房地产' : 'investmentRealEstate',
    '027固定资产' : 'fixedAssets',
    '028在建工程' : 'constructionInProgress',
    '029工程物资' : 'engineerMaterial',
    '030固定资产清理' : 'fixedAssetsCleanUp',
    '031生产性生物资产' : 'productiveBiologicalAssets',
    '032油气资产' : 'oilAndGasAssets',
    '033无形资产' : 'intangibleAssets',
    '034开发支出' : 'developmentExpenditure',
    '035商誉' : 'goodwill',
    '036长期待摊费用' : 'longTermDeferredExpenses',
    '037递延所得税资产' : 'deferredIncomeTaxAssets',
    '038其他非流动资产' : 'otherNonCurrentAssets',
    '039非流动资产合计' : 'totalNonCurrentAssets',
    '040资产总计' : 'totalAssets',
    # 2.2 负债
    # 2.2.1 流动负债
    '041短期借款' : 'shortTermLoan',
    '042交易性金融负债' : 'tradingFinancialLiabilities',
    '043应付票据' : 'billsPayable',
    '044应付账款' : 'accountsPayable',
    '045预收款项' : 'advancedReceivable',
    '046应付职工薪酬' : 'employeesPayable',
    '047应交税费' : 'taxPayable',
    '048应付利息' : 'interestPayable',
    '049应付股利' : 'dividendPayable',
    '050其他应付款' : 'otherPayable',
    '051应付关联公司款' : 'interCompanyPayable',
    '052一年内到期的非流动负债' : 'noncurrLiabilitiesDueOneYear',
    '053其他流动负债' : 'otherCurrentLiabilities',
    '054流动负债合计' : 'totalCurrentLiabilities',
    # 2.2.2 非流动负债
    '055长期借款' : 'longTermLoans',
    '056应付债券' : 'bondsPayable',
    '057长期应付款' : 'longTermPayable',
    '058专项应付款' : 'specialPayable',
    '059预计负债' : 'estimatedLiabilities',
    '060递延所得税负债' : 'defferredIncomeTaxLiabilities',
    '061其他非流动负债' : 'otherNonCurrentLiabilities',
    '062非流动负债合计' : 'totalNonCurrentLiabilities',
    '063负债合计' : 'totalLiabilities',
    # 2.3 所有者权益
    '064实收资本（或股本）' : 'totalShare',
    '065资本公积' : 'capitalReserve',
    '066盈余公积' : 'surplusReserve',
    '067减：库存股' : 'treasuryStock',
    '068未分配利润' : 'undistributedProfits',
    '069少数股东权益' : 'minorityEquity',
    '070外币报表折算价差' : 'foreignCurrenReportTransSpread',
    '071非正常经营项目收益调整' : 'abnorBusiProjectEarningsAdjust',
    '072所有者权益（或股东权益）合计' : 'totalOwnersEquity',
    '073负债和所有者（或股东权益）合计' : 'totalLiabilitiesAnOwnersEquity',
    # 3. 利润表
    '074其中：营业收入' : 'operatingRevenue',
    '075其中：营业成本' : 'operatingCosts',
    '076营业税金及附加' : 'taxAndSurcharges',
    '077销售费用' : 'salesCosts',
    '078管理费用' : 'managementCosts',
    '079堪探费用' : 'explorationCosts',
    '080财务费用' : 'financialCosts',
    '081资产减值损失' : 'assestsDevaluation',
    '082加：公允价值变动净收益' : 'profitLossFromFairValueChanges',
    '083投资收益' : 'investmentIncome',
    '084其中：对联营企业和合营企业的投资收益' : 'invesIncomFrAffilBusiCooperEn',
    '085影响营业利润的其他科目' : 'othSubAffectOperatProfit',
    '086三、营业利润' : 'operatingProfit',
    '087加：补贴收入' : 'subsidyIncome',
    '088营业外收入' : 'nonOperatingIncome',
    '089减：营业外支出' : 'nonOperatingExpenses',
    '090其中：非流动资产处置净损失' : 'netLossFrDisposOfNonCurrAssets',
    '091加：影响利润总额的其他科目' : 'otherSubjectsAffectTotalProfit',
    '092四、利润总额' : 'totalProfit',
    '093减：所得税' : 'incomeTax',
    '094加：影响净利润的其他科目' : 'otherSubjectsAffectNetProfit',
    '095五、净利润' : 'netProfit',
    '096归属于母公司所有者的净利润' : 'netProfitsBelToParComOwner',
    '097少数股东损益' : 'minorityProfitAndLoss',

    # 4. 现金流量表
    # 4.1 经营活动 Operating
    '098销售商品、提供劳务收到的现金' : 'cashFromGoodsSalOrRendOfServ',
    '099收到的税费返还' : 'refundOfTaxAndFeeReceived',
    '100收到其他与经营活动有关的现金' : 'otherCashRelaBusiActivReceived',
    '101经营活动现金流入小计' : 'cashInflowsFromOperatActiv',
    '102购买商品、接受劳务支付的现金' : 'buyGoodsReceivCashPaidLabor',
    '103支付给职工以及为职工支付的现金' : 'paymentToEmployCashPaidEmploy',
    '104支付的各项税费' : 'paymentsOfVariousTaxes',
    '105支付其他与经营活动有关的现金' : 'payOfOtherCashRelatToBusiActiv',
    '106经营活动现金流出小计' : 'cashOutOperaActiv',
    '107经营活动产生的现金流量净额' : 'netCashOperatActiv',
    # 4.2 投资活动 Investment
    '108收回投资收到的现金' : 'cashReceivFromInvestRece',
    '109取得投资收益收到的现金' : 'cashReceivedFromInvestIncome',
    '110处置固定资产、无形资产和其他长期资产收回的现金净额' : 'dispCashLongTermAssets',
    '111处置子公司及其他营业单位收到的现金净额' : 'dispNetCashReceivSubsBusiUnits',
    '112收到其他与投资活动有关的现金' : 'otherCashReceRelatInvestActiv',
    '113投资活动现金流入小计' : 'cashinFlowsFromInvestActiv',
    '114购建固定资产、无形资产和其他长期资产支付的现金' : 'cashPayLongTermAssets',
    '115投资支付的现金' : 'cashInvestment',
    '116取得子公司及其他营业单位支付的现金净额' : 'NetCashPaidBySubsBusiUnits',
    '117支付其他与投资活动有关的现金' : 'CashPaidRelatToInvestActiv',
    '118投资活动现金流出小计' : 'cashOutInvestActiv',
    '119投资活动产生的现金流量净额' : 'netCashFlowsFromInvestActiv',
    # 4.3 筹资活动 Financing
    '120吸收投资收到的现金' : 'cashReceivedFromInvestors',
    '121取得借款收到的现金' : 'cashFromBorrowings',
    '122收到其他与筹资活动有关的现金' : 'otherCashReceivRelatFinanActiv',
    '123筹资活动现金流入小计' : 'cashInflowsFromFinanActiv',
    '124偿还债务支付的现金' : 'cashPaymentsOfAmountBorrowed',
    '125分配股利、利润或偿付利息支付的现金' : 'cashPayDistDivProf',
    '126支付其他与筹资活动有关的现金' : 'otherCashPayRelatToFinanActiv',
    '127筹资活动现金流出小计' : 'cashOutflowsFromFinanActiv',
    '128筹资活动产生的现金流量净额' : 'netCashFlowsFromFinanActiv',
    # 4.4 汇率变动
    '129四、汇率变动对现金的影响' : 'effOfForeExchRateChangesOnCash',
    '130四(2)、其他原因对现金的影响' : 'effectOfOtherReasonOnCash',
    # 4.5 现金及现金等价物净增加
    '131五、现金及现金等价物净增加额' : 'netIncCashCashEquiv',
    '132期初现金及现金等价物余额' : 'initialCashAndCashEquivBalan',
    # 4.6 期末现金及现金等价物余额
    '133期末现金及现金等价物余额' : 'theFinalCashAndCashEquivBalan',
    # 4.x 补充项目 Supplementary Schedule：
    # 现金流量附表项目    Indirect Method
    # 4.x.1 将净利润调节为经营活动现金流量 Convert net profit to cash flow from operating activities
    '134净利润' : 'netProfitFromOperatActiv',
    '135资产减值准备' : 'provisionForAssetsLosses',
    '136固定资产折旧、油气资产折耗、生产性生物资产折旧' : 'deprecForFixedAssets',
    '137无形资产摊销' : 'amortizationOfIntangibleAssets',
    '138长期待摊费用摊销' : 'cLongtermDeferredExpenses',
    '139处置固定资产、无形资产和其他长期资产的损失' : 'lossDispLongtermAssets',
    '140固定资产报废损失' : 'scrapLossOfFixedAssets',
    '141公允价值变动损失' : 'lossFromFairValueChange',
    '142财务费用' : 'financialExpenses',
    '143投资损失' : 'investmentLosses',
    '144递延所得税资产减少' : 'decreaseOfDeferredTaxAssets',
    '145递延所得税负债增加' : 'incrOfDeferredTaxLiabilities',
    '146存货的减少' : 'decreaseOfInventory',
    '147经营性应收项目的减少' : 'decreaseOfOperationReceivables',
    '148经营性应付项目的增加' : 'increaseOfOperationPayables',
    '149其他' : 'others',
    '150经营活动产生的现金流量净额2' : 'netCashFromOperatingActiv2',
    # 4.x.2 不涉及现金收支的投资和筹资活动 Investing and financing activities not involved in cash
    '151债务转为资本' : 'debtConvertedToCSapital',
    '152一年内到期的可转换公司债券' : 'convertibleBondMaturityOneYear',
    '153融资租入固定资产' : 'leaseholdImprovements',
    # 4.x.3 现金及现金等价物净增加情况 Net increase of cash and cash equivalents
    '154现金的期末余额' : 'cashEndingBal',
    '155现金的期初余额' : 'cashBeginingBal',
    '156现金等价物的期末余额' : 'cashEquivalentsEndingBal',
    '157现金等价物的期初余额' : 'cashEquivalentsBeginningBal',
    '158现金及现金等价物净增加额' : 'netIncrCashCashEquivalents',
    # 5. 偿债能力分析
    '159流动比率' : 'currentRatio',
    '160速动比率' : 'acidTestRatio',
    '161现金比率(%)' : 'cashRatio',
    '162利息保障倍数' : 'interestCoverageRatio',
    '163非流动负债比率(%)' : 'noncurrentLiabilitiesRatio',
    '164流动负债比率(%)' : 'currentLiabilitiesRatio',
    '165现金到期债务比率(%)' : 'cashDebtRatio',
    '166有形资产净值债务率(%)' : 'debtToTangibleAssetsRatio',
    '167权益乘数(%)' : 'equityMultiplier',
    '168股东的权益/负债合计(%)' : 'equityDebtRatio',
    '169有形资产/负债合计(%)' : 'tangibleAssetDebtRatio',
    '170经营活动产生的现金流量净额/负债合计(%)' : 'netCashFlowsOperaActivDebRatio',
    '171EBITDA/负债合计(%)' : 'EBITDA/Liabilities',
    # 6. 经营效率分析
    # 销售收入÷平均应收账款=销售收入\(0.5 x(应收账款期初+期末))
    '172应收帐款周转率' : 'turnoverRatioOfReceivable;',
    '173存货周转率' : 'turnoverRatioOfInventory',
    # (存货周转天数+应收帐款周转天数-应付帐款周转天数+预付帐款周转天数-预收帐款周转天数)/365
    '174运营资金周转率' : 'turnoverRatioOfOperatingAssets',
    '175总资产周转率' : 'turnoverRatioOfTotalAssets',
    '176固定资产周转率' : 'turnoverRatioOfFixedAssets',
    '177应收帐款周转天数' : 'daysSalesOutstanding',
    '178存货周转天数' : 'daysSalesOfInventory',
    '179流动资产周转率' : 'turnoverRatioOfCurrentAssets',
    '180流动资产周转天数' : 'daysSalesofCurrentAssets',
    '181总资产周转天数' : 'daysSalesofTotalAssets',
    '182股东权益周转率' : 'equityTurnover',
    # 7. 发展能力分析
    '183营业收入增长率(%)' : 'operatingIncomeGrowth',
    '184净利润增长率(%)' : 'netProfitGrowthRate',
    '185净资产增长率(%)' : 'netAssetsGrowthRate',
    '186固定资产增长率(%)' : 'fixedAssetsGrowthRate',
    '187总资产增长率(%)' : 'totalAssetsGrowthRate',
    '188投资收益增长率(%)' : 'investmentIncomeGrowthRate',
    '189营业利润增长率(%)' : 'operatingProfitGrowthRate',
    '190暂无' : 'None1',
    '191暂无' : 'None2',
    '192暂无' : 'None3',
    # 8. 获利能力分析
    '193成本费用利润率(%)' : 'rateOfReturnOnCost',
    '194营业利润率' : 'rateOfReturnOnOperatingProfit',
    '195营业税金率' : 'rateOfReturnOnBusinessTax',
    '196营业成本率' : 'rateOfReturnOnOperatingCost',
    '197净资产收益率' : 'rateReturnComStockholdEq',
    '198投资收益率' : 'rateOfReturnOnInvestmentIncome',
    '199销售净利率(%)' : 'rateOfReturnOnNetSalesProfit',
    '200总资产报酬率' : 'rateOfReturnOnTotalAssets',
    '201净利润率' : 'netProfitMargin',
    '202销售毛利率(%)' : 'rateGrossProfitFromSales',
    '203三费比重' : 'threeFeeProportion',
    '204管理费用率' : 'ratioOfChargingExpense',
    '205财务费用率' : 'ratioOfFinancialExpense',
    '206扣除非经常性损益后的净利润' : 'netProAftExtrGainLoss',
    '207息税前利润(EBIT)' : 'EBIT',
    '208息税折旧摊销前利润(EBITDA)' : 'EBITDA',
    '209EBITDA/营业总收入(%)' : 'EBITDA/GrossRevenueRate',
    # 9. 资本结构分析
    '210资产负债率(%)' : 'assetsLiabilitiesRatio',
    '211流动资产比率' : 'currentAssetsRatio',
    '212货币资金比率' : 'monetaryFundRatio',
    '213存货比率' : 'inventoryRatio',
    '214固定资产比率' : 'fixedAssetsRatio',
    '215负债结构比' : 'liabilitiesStructureRatio',
    '216归属于母公司股东权益/全部投入资本(%)' : 'shareholdOwnPaCompTotalCapital',
    '217股东的权益/带息债务(%)' : 'shareholdInterestRateDebRatio',
    '218有形资产/净债务(%)' : 'tangibleAssets/NetDebtRatio',
    # 10. 现金流量分析
    '219每股经营性现金流(元)' : 'coperatingCashFlowPerShare',
    '220营业收入现金含量(%)' : 'cashOfOperatingIncome',
    '221经营活动产生的现金流量净额/经营活动净收益(%)' : 'netOperaCashFlownetOperaProfit',
    '222销售商品提供劳务收到的现金/营业收入(%)' : 'cashFromGoodsSalesOperaRevenue',
    '223经营活动产生的现金流量净额/营业收入' : 'netOperaCashFlowOperaRevenue',
    '224资本支出/折旧和摊销' : 'capExpendDepreAmort',
    '225每股现金流量净额(元)' : 'netCashFlowPerShare',
    '226经营净现金比率（短期债务）' : 'operaCashFlowShortTermDebRatio',
    '227经营净现金比率（全部债务）' : 'operaCashFlowLongTermDebRatio',
    '228经营活动现金净流量与净利润比率' : 'OperacashFlowOfNetProRatio',
    '229全部资产现金回收率' : 'cashRecoveryForAllAssets',
    # 11. 单季度财务指标
    '230营业收入' : 'operatingRevenueSingle',
    '231营业利润' : 'operatingProfitSingle',
    '232归属于母公司所有者的净利润' : 'netProBelonToOwnerParCompySing',
    '233扣除非经常性损益后的净利润' : 'netProfitAfterExtrGainLossSing',
    '234经营活动产生的现金流量净额' : 'netCashFlowsFromOperaActivSing',
    '235投资活动产生的现金流量净额' : 'netCashFlowsFromInvesActivSing',
    '236筹资活动产生的现金流量净额' : 'netCashFlowsFromFinanActivSing',
    '237现金及现金等价物净增加额' : 'netIncrCashCashEquivaSingle',
    # 12.股本股东
    '238总股本' : 'totalCapital',
    '239已上市流通A股' : 'listedAShares',
    '240已上市流通B股' : 'listedBShares',
    '241已上市流通H股' : 'listedHShares',
    '242股东人数(户)' : 'numberOfShareholders',
    '243第一大股东的持股数量' : 'theNumOfFirstMajShareholder',
    '244十大流通股东持股数量合计(股)' : 'totalNumTopTenCircShareholder',
    '245十大股东持股数量合计(股)' : 'totalNumberTopTenShareholder',
    # 13.机构持股
    '246机构总量（家）' : 'institutionNumber',
    '247机构持股总量(股)' : 'institutionShareholding',
    '248QFII机构数' : 'QFIIInstitutionNumber',
    '249QFII持股量' : 'QFIIShareholding',
    '250券商机构数' : 'brokerNumber',
    '251券商持股量' : 'brokerShareholding',
    '252保险机构数' : 'securityNumber',
    '253保险持股量' : 'securityShareholding',
    '254基金机构数' : 'fundsNumber',
    '255基金持股量' : 'fundsShareholding',
    '256社保机构数' : 'socialSecurityNumber',
    '257社保持股量' : 'socialSecurityShareholding',
    '258私募机构数' : 'privateEquityNumber',
    '259私募持股量' : 'privateEquityShareholding',
    '260财务公司机构数' : 'financialCompanyNumber',
    '261财务公司持股量' : 'financialCompanyShareholding',
    '262年金机构数' : 'pensionInsuranceAgencyNumber',
    '263年金持股量' : 'pensInsuranAgShareholf',
    # 14.新增指标
    # [注：季度报告中，若股东同时持有非流通A股性质的股份(如同时持有流通A股和流通B股），取的是包含同时持有非流通A股性质的流通股数]
    '264十大流通股东中持有A股合计(股)' : 'totalANumberTopTenShareholder',
    '265第一大流通股东持股量(股)' : 'firstLarCirculShareholdersNum',
    # [注：1.自由流通股=已流通A股-十大流通股东5%以上的A股；2.季度报告中，若股东同时持有非流通A股性质的股份(如同时持有流通A股和流通H股），5%以上的持股取的是不包含同时持有非流通A股性质的流通股数，结果可能偏大； 3.指标按报告期展示，新股在上市日的下个报告期才有数据]
    '266自由流通股(股)' : 'freeCirculationStock',
    '267受限流通A股(股)' : 'limitedCirculationAShares',
    '268一般风险准备(金融类)' : 'generalRiskPreparation',
    '269其他综合收益(利润表)' : 'otherComprehensiveIncome',
    '270综合收益总额(利润表)' : 'totalComprehensiveIncome',
    '271归属于母公司股东权益(资产负债表)' : 'shareholdOwnershipOfAParComp',
    '272银行机构数(家)(机构持股)' : 'bankInstutionNumber',
    '273银行持股量(股)(机构持股)' : 'bankInstutionShareholding',
    '274一般法人机构数(家)(机构持股)' : 'corporationNumber',
    '275一般法人持股量(股)(机构持股)' : 'corporationShareholding',
    '276近一年净利润(元)' : 'netProfitLastYear',
    '277信托机构数(家)(机构持股)' : 'trustInstitutionNumber',
    '278信托持股量(股)(机构持股)' : 'trustInstitutionShareholding',
    '279特殊法人机构数(家)(机构持股)' : 'specialCorporationNumber',
    '280特殊法人持股量(股)(机构持股)' : 'specialCorporationShareholding',
    '281加权净资产收益率(每股指标)' : 'weightedROE',
    '282扣非每股收益(单季度财务指标)' : 'nonEPSSingle',
    '283最近一年营业收入(万元)': 'lastYearOperatingIncome',
    '284国家队持股数量(万股)': 'nationalTeamShareholding',
    #[注：本指标统计包含汇金公司、证金公司、外汇管理局旗下投资平台、国家队基金、国开、养老金以及中科汇通等国家队机构持股数量]
    '285业绩预告-本期净利润同比增幅下限%': 'PF_theLowerLimitoftheYearonyearGrowthofNetProfitForThePeriod',
    #[注：指标285至294展示未来一个报告期的数据。例，3月31日至6月29日这段时间内展示的是中报的数据；如果最新的财务报告后面有多个报告期的业绩预告/快报，只能展示最新的财务报告后面的一个报告期的业绩预告/快报]
    '286业绩预告-本期净利润同比增幅上限%': 'PF_theHigherLimitoftheYearonyearGrowthofNetProfitForThePeriod',
    '287业绩快报-归母净利润': 'PE_RETTOTHEMOTHERSNETPROFIT',
    '288业绩快报-扣非净利润': 'PE_Non-netProfit',
    '289业绩快报-总资产': 'PE_TotalAssets',
    '290业绩快报-净资产': 'PE_NetAssets',
    '291业绩快报-每股收益': 'PE_EPS',
    '292业绩快报-摊薄净资产收益率': 'PE_DilutedROA',
    '293业绩快报-加权净资产收益率': 'PE_WeightedROE',
    '294业绩快报-每股净资产': 'PE_NetAssetsperShare',
    '295应付票据及应付账款(资产负债表)': 'BS_NotesPayableandAccountsPayable',
    '296应收票据及应收账款(资产负债表)': 'BS_NotesReceivableandAccountsReceivable',
    '297递延收益(资产负债表)': 'BS_DeferredIncome',
    '298其他综合收益(资产负债表)': 'BS_OtherComprehensiveIncome',
    '299其他权益工具(资产负债表)': 'BS_OtherEquityInstruments',
    '300其他收益(利润表)': 'IS_OtherIncome',
    '301资产处置收益(利润表)': 'IS_AssetDisposalIncome',
    '302持续经营净利润(利润表)': 'IS_NetProfitforContinuingOperations',
    '303终止经营净利润(利润表)': 'IS_NetProfitforTerminationOperations',
    '304研发费用(利润表)': 'IS_R&DExpense',
    '305其中:利息费用(利润表-财务费用)': 'IS_InterestExpense',
    '306其中:利息收入(利润表-财务费用)': 'IS_InterestIncome',
    '307近一年经营活动现金流净额': 'netCashFlowfromOperatingActivitiesinthepastyear',
    '308未知308':'unknown308',
    '309未知309':'unknown309',
    '310未知310':'unknown310',
    '311未知311':'unknown311',
    '312未知312':'unknown312',
    '313未知313':'unknown313',
    '314未知314':'unknown314',
    '315未知315':'unknown315',
    '316未知316':'unknown316',
    '317未知317':'unknown317',
    '318未知318':'unknown318',

    '319未知319':'unknown319',
    '320未知320':'unknown320',
    '321未知321':'unknown321',
    '322未知322':'unknown322',
    '323未知323':'unknown323',
    '324未知324':'unknown324',
    '325未知325':'unknown325',
    '326未知326':'unknown326',
    '327未知327':'unknown327',
    '328未知328':'unknown328',
    '329未知329':'unknown329',
    '330未知330':'unknown330',
    '331未知331':'unknown331',
    '332未知332':'unknown332',
    '333未知333':'unknown333',
    '334未知334':'unknown334',
    '335未知335':'unknown335',
    '336未知336':'unknown336',
    '337未知337':'unknown337',
    '338未知338':'unknown338',
    '339未知339':'unknown339',
    '340未知340':'unknown340',
    '341未知341':'unknown341',
    '342未知342':'unknown342',
    '343未知343':'unknown343',
    '344未知344':'unknown344',
    '345未知345':'unknown345',
    '346未知346':'unknown346',
    '347未知347':'unknown347',
    '348未知348':'unknown348',
    '349未知349':'unknown349',
    '350未知350':'unknown350',
    '351未知351':'unknown351',
    '352未知352':'unknown352',
    '353未知353':'unknown353',
    '354未知354':'unknown354',
    '355未知355':'unknown355',
    '356未知356':'unknown356',
    '357未知357':'unknown357',
    '358未知358':'unknown358',
    '359未知359':'unknown359',
    '360未知360':'unknown360',
    '361未知361':'unknown361',
    '362未知362':'unknown362',
    '363未知363':'unknown363',
    '364未知364':'unknown364',
    '365未知365':'unknown365',
    '366未知366':'unknown366',
    '367未知367':'unknown367',
    '368未知368':'unknown368',
    '369未知369':'unknown369',
    '370未知370':'unknown370',
    '371未知371':'unknown371',
    '372未知372':'unknown372',
    '373未知373':'unknown373',
    '374未知374':'unknown374',
    '375未知375':'unknown375',
    '376未知376':'unknown376',
    '377未知377':'unknown377',
    '378未知378':'unknown378',
    '379未知379':'unknown379',
    '380未知380':'unknown380',
    '381未知381':'unknown381',
    '382未知382':'unknown382',
    '383未知383':'unknown383',
    '384未知384':'unknown384',
    '385未知385':'unknown385',
    '386未知386':'unknown386',
    '387未知387':'unknown387',
    '388未知388':'unknown388',
    '389未知389':'unknown389',
    '390未知390':'unknown390',
    '391未知391':'unknown391',
    '392未知392':'unknown392',
    '393未知393':'unknown393',
    '394未知394':'unknown394',
    '395未知395':'unknown395',
    '396未知396':'unknown396',
    '397未知397':'unknown397',
    '398未知398':'unknown398',
    '399未知399':'unknown399',
    '400未知400':'unknown400',
    '401未知401':'unknown401',
    '402未知402':'unknown402',
    '403未知403':'unknown403',
    '404未知404':'unknown404',
    '405未知405':'unknown405',
    '406未知406':'unknown406',
    '407未知407':'unknown407',
    '408未知408':'unknown408',
    '409未知409':'unknown409',
    '410未知410':'unknown410',
    '411未知411':'unknown411',
    '412未知412':'unknown412',
    '413未知413':'unknown413',
    '414未知414':'unknown414',
    '415未知415':'unknown415',
    '416未知416':'unknown416',
    '417未知417':'unknown417',
    '418未知418':'unknown418',
    '419未知419':'unknown419',
    '420未知420':'unknown420',
    '421未知421':'unknown421',
    '422未知422':'unknown422',
    '423未知423':'unknown423',
    '424未知424':'unknown424',
    '425未知425':'unknown425',
    '426未知426':'unknown426',
    '427未知427':'unknown427',
    '428未知428':'unknown428',
    '429未知429':'unknown429',
    '430未知430':'unknown430',
    '431未知431':'unknown431',
    '432未知432':'unknown432',
    '433未知433':'unknown433',
    '434未知434':'unknown434',
    '435未知435':'unknown435',
    '436未知436':'unknown436',
    '437未知437':'unknown437',
    '438未知438':'unknown438',
    '439未知439':'unknown439',
    '440未知440':'unknown440',
    '441未知441':'unknown441',
    '442未知442':'unknown442',
    '443未知443':'unknown443',
    '444未知444':'unknown444',
    '445未知445':'unknown445',
    '446未知446':'unknown446',
    '447未知447':'unknown447',
    '448未知448':'unknown448',
    '449未知449':'unknown449',
    '450未知450':'unknown450',
    '451未知451':'unknown451',
    '452未知452':'unknown452',
    '453未知453':'unknown453',
    '454未知454':'unknown454',
    '455未知455':'unknown455',
    '456未知456':'unknown456',
    '457未知457':'unknown457',
    '458未知458':'unknown458',
    '459未知459':'unknown459',
    '460未知460':'unknown460',
    '461未知461':'unknown461',
    '462未知462':'unknown462',
    '463未知463':'unknown463',
    '464未知464':'unknown464',
    '465未知465':'unknown465',
    '466未知466':'unknown466',
    '467未知467':'unknown467',
    '468未知468':'unknown468',
    '469未知469':'unknown469',
    '470未知470':'unknown470',
    '471未知471':'unknown471',
    '472未知472':'unknown472',
    '473未知473':'unknown473',
    '474未知474':'unknown474',
    '475未知475':'unknown475',
    '476未知476':'unknown476',
    '477未知477':'unknown477',
    '478未知478':'unknown478',
    '479未知479':'unknown479',
    '480未知480':'unknown480',
    '481未知481':'unknown481',
    '482未知482':'unknown482',
    '483未知483':'unknown483',
    '484未知484':'unknown484',
    '485未知485':'unknown485',
    '486未知486':'unknown486',
    '487未知487':'unknown487',
    '488未知488':'unknown488',
    '489未知489':'unknown489',
    '490未知490':'unknown490',
    '491未知491':'unknown491',
    '492未知492':'unknown492',
    '493未知493':'unknown493',
    '494未知494':'unknown494',
    '495未知495':'unknown495',
    '496未知496':'unknown496',
    '497未知497':'unknown497',
    '498未知498':'unknown498',
    '499未知499':'unknown499',
    '500未知500':'unknown500',
    '501未知501':'unknown501',
    '502未知502':'unknown502',
    '503未知503':'unknown503',
    '504未知504':'unknown504',
    '505未知505':'unknown505',
    '506未知506':'unknown506',
    '507未知507':'unknown507',
    '508未知508':'unknown508',
    '509未知509':'unknown509',
    '510未知510':'unknown510',
    '511未知511':'unknown511',
    '512未知512':'unknown512',
    '513未知513':'unknown513',
    '514未知514':'unknown514',
    '515未知515':'unknown515',
    '516未知516':'unknown516',
    '517未知517':'unknown517',
    '518未知518':'unknown518',
    '519未知519':'unknown519',
    '520未知520':'unknown520',
    '521未知521':'unknown521',
    '522未知522':'unknown522',
    '523未知523':'unknown523',
    '524未知524':'unknown524',
    '525未知525':'unknown525',
    '526未知526':'unknown526',
    '527未知527':'unknown527',
    '528未知528':'unknown528',
    '529未知529':'unknown529',
    '530未知530':'unknown530',
    '531未知531':'unknown531',
    '532未知532':'unknown532',
    '533未知533':'unknown533',
    '534未知534':'unknown534',
    '535未知535':'unknown535',
    '536未知536':'unknown536',
    '537未知537':'unknown537',
    '538未知538':'unknown538',
    '539未知539':'unknown539',
    '540未知540':'unknown540',
    '541未知541':'unknown541',
    '542未知542':'unknown542',
    '543未知543':'unknown543',
    '544未知544':'unknown544',
    '545未知545':'unknown545',
    '546未知546':'unknown546',
    '547未知547':'unknown547',
    '548未知548':'unknown548',
    '549未知549':'unknown549',
    '550未知550':'unknown550',
    '551未知551':'unknown551',
    '552未知552':'unknown552',
    '553未知553':'unknown553',
    '554未知554':'unknown554',
    '555未知555':'unknown555',
    '556未知556':'unknown556',
    '557未知557':'unknown557',
    '558未知558':'unknown558',
    '559未知559':'unknown559',
    '560未知560':'unknown560',
    '561未知561':'unknown561',
    '562未知562':'unknown562',
    '563未知563':'unknown563',
    '564未知564':'unknown564',
    '565未知565':'unknown565',
    '566未知566':'unknown566',
    '567未知567':'unknown567',
    '568未知568':'unknown568',
    '569未知569':'unknown569',
    '570未知570':'unknown570',
    '571未知571':'unknown571',
    '572未知572':'unknown572',
    '573未知573':'unknown573',
    '574未知574':'unknown574',
    '575未知575':'unknown575',
    '576未知576':'unknown576',
    '577未知577':'unknown577',
    '578未知578':'unknown578',
    '579未知579':'unknown579',
    '580未知580':'unknown580',
    '581未知581':'unknown581',
    '582未知582':'unknown582',
    '583未知583':'unknown583',
    '584未知584':'unknown584',
    '585未知585':'unknown585',
    '586未知586':'unknown586',
    '587未知587':'unknown587',
    '588未知588':'unknown588',
    '589未知589':'unknown589',
    '590未知590':'unknown590',
    '591未知591':'unknown591',
    '592未知592':'unknown592',
    '593未知593':'unknown593',
}

financial_dict1 = {
    '流动资产':'',
    '货币资金(元)':'moneyFunds',
    '以公允价值计量且其变动计入当期损益的金融资产(元)':'tradingFinancialAssets',
    '应收票据及应收账款(元)':'',
    '其中：应收票据(元)':'billsReceivables',
    '应收账款(元)':'accountsReceivables',
    '预付款项(元)':'prepayments',
    '其他应收款合计(元)':'',
    '其他应收款(元)':'otherReceivables',
    '存货(元)':'inventory',
    '一年内到期的非流动资产(元)':'noncurrAssetsDueOneYear',
    '其他流动资产(元)':'otherLiquidAssets',
    '流动资产合计(元)':'totalLiquidAssets',
    '非流动资产':'totalNonCurrentAssets',
    '可供出售金融资产(元)':'availableForSaleSecurities',
    '长期股权投资(元)':'longTermEquityInvestment',
    '投资性房地产(元)':'investmentRealEstate',
    '固定资产合计(元)':'',
    '其中：固定资产(元)':'fixedAssets',
    '固定资产清理(元)':'fixedAssetsCleanUp',
    '在建工程合计(元)':'',
    '其中：在建工程(元)':'constructionInProgress',
    '工程物资(元)':'engineerMaterial',
    '无形资产(元)':'intangibleAssets',
    '商誉(元)':'goodwill',
    '长期待摊费用(元)':'longTermDeferredExpenses',
    '递延所得税资产(元)':'deferredIncomeTaxAssets',
    '其他非流动资产(元)':'otherNonCurrentAssets',
    '非流动资产合计(元)':'totalNonCurrentAssets',
    '资产合计(元)':'totalAssets',
    '流动负债':'',
    '短期借款(元)':'shortTermLoan',
    '应付票据及应付账款(元)':'',
    '其中：应付票据(元)':'billsPayable',
    '应付账款(元)':'accountsPayable',
    '预收款项(元)':'advancedReceivable',
    '应付职工薪酬(元)':'employeesPayable',
    '应交税费(元)':'taxPayable',
    '其他应付款合计(元)':'',
    '其中：应付利息(元)':'interestPayable',
    '应付股利(元)':'dividendPayable',
    '其他应付款(元)':'otherPayable',
    '一年内到期的非流动负债(元)':'noncurrLiabilitiesDueOneYear',
    '其他流动负债(元)':'otherCurrentLiabilities',
    '流动负债合计(元)':'totalCurrentLiabilities',
    '非流动负债':'',
    '长期借款(元)':'longTermLoans',
    '应付债券(元)':'bondsPayable',
    '长期应付款合计(元)':'',
    '其中：长期应付款(元)':'longTermPayable',
    '专项应付款(元)':'specialPayable',
    '预计负债(元)':'estimatedLiabilities',
    '递延所得税负债(元)':'defferredIncomeTaxLiabilities',
    '递延收益-非流动负债(元)':'',
    '其他非流动负债(元)':'otherNonCurrentLiabilities',
    '非流动负债合计(元)':'totalNonCurrentLiabilities',
    '负债合计(元)':'totalLiabilities',
    '所有者权益（或股东权益）':'',
    '实收资本（或股本）(元)':'totalShare',
    '资本公积(元)':'capitalReserve',
    '其他综合收益(元)':'',
    '盈余公积(元)':'surplusReserve',
    '未分配利润(元)':'undistributedProfits',
    '归属于母公司所有者权益合计(元)':'',
    '少数股东权益(元)':'minorityEquity',
    '所有者权益（或股东权益）合计(元)':'totalOwnersEquity',
    '负债和所有者权益（或股东权益）合计(元)':'totalLiabilitiesAnOwnersEquity',
    '一、营业总收入(元)':'',
    '其中：营业收入(元)':'operatingRevenue',
    '二、营业总成本(元)':'',
    '其中：营业成本(元)':'operatingCosts',
    '营业税金及附加(元)':'taxAndSurcharges',
    '销售费用(元)':'salesCosts',
    '管理费用(元)':'managementCosts',
    '研发费用(元)':'',
    '财务费用(元)':'financialCosts',
    '其中：利息费用(元)':'',
    '利息收入(元)':'',
    '资产减值损失(元)':'assestsDevaluation',
    '加：公允价值变动收益(元)':'profitLossFromFairValueChanges',
    '投资收益(元)':'investmentIncome',
    '其中：联营企业和合营企业的投资收益(元)':'invesIncomFrAffilBusiCooperEn',
    '资产处置收益(元)':'',
    '其他收益(元)':'othSubAffectOperatProfit',
    '三、营业利润(元)':'operatingProfit',
    '加：营业外收入(元)':'nonOperatingIncome',
    '其中：非流动资产处置利得(元)':'',
    '减：营业外支出(元)':'nonOperatingExpenses',
    '其中：非流动资产处置损失(元)':'netLossFrDisposOfNonCurrAssets',
    '四、利润总额(元)':'totalProfit',
    '减：所得税费用(元)':'incomeTax',
    '五、净利润(元)':'netProfit',
    '（一）持续经营净利润(元)':'',
    '归属于母公司所有者的净利润(元)':'netProfitsBelToParComOwner',
    '少数股东损益(元)':'minorityProfitAndLoss',
    '扣除非经常性损益后的净利润(元)':'netProAftExtrGainLoss',
    '六、每股收益':'',
    '（一）基本每股收益(元)':'',
    '（二）稀释每股收益(元)':'',
    '七、其他综合收益(元)':'',
    '归属母公司所有者的其他综合收益(元)':'',
    '八、综合收益总额(元)':'',
    '归属于母公司股东的综合收益总额(元)':'',
    '归属于少数股东的综合收益总额(元)':'',
    '一、经营活动产生的现金流量':'',
    '销售商品、提供劳务收到的现金(元)':'cashFromGoodsSalOrRendOfServ',
    '收到的税费与返还(元)':'refundOfTaxAndFeeReceived',
    '收到其他与经营活动有关的现金(元)':'otherCashRelaBusiActivReceived',
    '经营活动现金流入小计(元)':'cashInflowsFromOperatActiv',
    '购买商品、接受劳务支付的现金(元)':'buyGoodsReceivCashPaidLabor',
    '支付给职工以及为职工支付的现金(元)':'paymentToEmployCashPaidEmploy',
    '支付的各项税费(元)':'paymentsOfVariousTaxes',
    '支付其他与经营活动有关的现金(元)':'payOfOtherCashRelatToBusiActiv',
    '经营活动现金流出小计(元)':'cashOutOperaActiv',
    '经营活动产生的现金流量净额(元)':'netCashOperatActiv',
    '二、投资活动产生的现金流量':'',
    '收回投资收到的现金(元)':'cashReceivFromInvestRece',
    '取得投资收益收到的现金(元)':'cashReceivedFromInvestIncome',
    '处置固定资产、无形资产和其他长期资产收回的现金净额(元)':'dispCashLongTermAssets',
    '处置子公司及其他营业单位收到的现金净额(元)':'dispNetCashReceivSubsBusiUnits',
    '收到其他与投资活动有关的现金(元)':'otherCashReceRelatInvestActiv',
    '投资活动现金流入小计(元)':'cashinFlowsFromInvestActiv',
    '购建固定资产、无形资产和其他长期资产支付的现金(元)':'cashPayLongTermAssets',
    '投资支付的现金(元)':'cashInvestment',
    '取得子公司及其他营业单位支付的现金净额(元)':'NetCashPaidBySubsBusiUnits',
    '支付其他与投资活动有关的现金(元)':'CashPaidRelatToInvestActiv',
    '投资活动现金流出小计(元)':'cashOutInvestActiv',
    '投资活动产生的现金流量净额(元)':'netCashFlowsFromInvestActiv',
    '三、筹资活动产生的现金流量':'',
    '吸收投资收到的现金(元)':'cashReceivedFromInvestors',
    '其中：子公司吸收少数股东投资收到的现金(元)':'',
    '取得借款收到的现金(元)':'cashFromBorrowings',
    '发行债券收到的现金(元)':'',
    '收到其他与筹资活动有关的现金(元)':'otherCashReceivRelatFinanActiv',
    '筹资活动现金流入小计(元)':'cashInflowsFromFinanActiv',
    '偿还债务支付的现金(元)':'cashPaymentsOfAmountBorrowed',
    '分配股利、利润或偿付利息支付的现金(元)':'cashPayDistDivProf',
    '其中：子公司支付给少数股东的股利、利润(元)':'',
    '支付其他与筹资活动有关的现金(元)':'otherCashPayRelatToFinanActiv',
    '筹资活动现金流出小计(元)':'cashOutflowsFromFinanActiv',
    '筹资活动产生的现金流量净额(元)':'netCashFlowsFromFinanActiv',
    '四、汇率变动对现金及现金等价物的影响(元)':'effOfForeExchRateChangesOnCash',
    '五、现金及现金等价物净增加额(元)':'netIncCashCashEquiv',
    '加：期初现金及现金等价物余额(元)':'initialCashAndCashEquivBalan',
    '六、期末现金及现金等价物余额(元)':'theFinalCashAndCashEquivBalan',
    '补充资料：':'',
    '1、将净利润调节为经营活动现金流量：':'',
    '净利润(元)':'netProfitFromOperatActiv',
    '加：资产减值准备(元)':'provisionForAssetsLosses',
    '固定资产折旧、油气资产折耗、生产性生物资产折旧(元)':'deprecForFixedAssets',
    '无形资产摊销(元)':'amortizationOfIntangibleAssets',
    '长期待摊费用摊销(元)':'cLongtermDeferredExpenses',
    '处置固定资产、无形资产和其他长期资产的损失(元)':'lossDispLongtermAssets',
    '固定资产报废损失(元)':'scrapLossOfFixedAssets',
    '公允价值变动损失(元)':'lossFromFairValueChange',
    '财务费用(元)':'financialCosts',
    '投资损失(元)':'investmentLosses',
    '递延所得税资产减少(元)':'decreaseOfDeferredTaxAssets',
    '递延所得税负债增加(元)':'incrOfDeferredTaxLiabilities',
    '存货的减少(元)':'decreaseOfInventory',
    '经营性应收项目的减少(元)':'decreaseOfOperationReceivables',
    '经营性应付项目的增加(元)':'increaseOfOperationPayables',
    '其他(元)':'others',
    '间接法-经营活动产生的现金流量净额(元)':'netCashFromOperatingActiv2',
    '2、不涉及现金收支的重大投资和筹资活动：':'',
    '债务转为资本(元)':'debtConvertedToCSapital',
    '3、现金及现金等价物净变动情况：':'',
    '现金的期末余额(元)':'cashEndingBal',
    '减：现金的期初余额(元)':'cashBeginingBal',
    '间接法-现金及现金等价物净增加额(元)':'netIncrCashCashEquivalents'
}

dict2= {'货币资金':'moneyFunds',
        '交易性金融资产':'tradingFinancialAssets',
        '应收票据':'billsReceivables',
        '应收账款':'accountsReceivables',
        '预付款项':'prepayments',
        '其他应收款':'otherReceivables',
        '应收利息':'interestReceivables',
        '应收股利':'dividendsReceivables',
        '存货':'inventory',
        '一年内到期的非流动资产':'noncurrAssetsDueOneYear',
        '其他流动资产':'otherLiquidAssets',
        '流动资产合计':'totalLiquidAssets',
        '可供出售金融资产':'availableForSaleSecurities',
        '持有至到期投资':'heldToMaturityInvestments',
        '长期应收款':'longTermReceivables',
        '长期股权投资':'longTermEquityInvestment',
        '投资性房地产':'investmentRealEstate',
        '固定资产':'fixedAssets',
        '在建工程':'constructionInProgress',
        '工程物资':'engineerMaterial',
        '固定资产清理':'fixedAssetsCleanUp',
        '生产性生物资产':'productiveBiologicalAssets',
        '油气资产':'oilAndGasAssets',
        '无形资产':'intangibleAssets',
        '开发支出':'developmentExpenditure',
        '商誉':'goodwill',
        '长期待摊费用':'longTermDeferredExpenses',
        '递延所得税资产':'deferredIncomeTaxAssets',
        '其他非流动资产':'otherNonCurrentAssets',
        '非流动资产合计':'totalNonCurrentAssets',
        '资产总计':'totalAssets',
        '短期借款':'shortTermLoan',
        '交易性金融负债':'tradingFinancialLiabilities',
        '应付票据':'billsPayable',
        '应付账款':'accountsPayable',
        '预收账款':'advancedReceivable',
        '应付职工薪酬':'employeesPayable',
        '应交税费':'taxPayable',
        '应付利息':'interestPayable',
        '应付股利':'dividendPayable',
        '其他应付款':'otherPayable',
        '一年内到期的非流动负债':'noncurrLiabilitiesDueOneYear',
        '其他流动负债':'otherCurrentLiabilities',
        '流动负债合计':'totalCurrentLiabilities',
        '长期借款':'longTermLoans',
        '应付债券':'bondsPayable',
        '长期应付款':'longTermPayable',
        '专项应付款':'specialPayable',
        '预计负债':'estimatedLiabilities',
        '递延所得税负债':'defferredIncomeTaxLiabilities',
        '其他非流动负债':'otherNonCurrentLiabilities',
        '非流动负债合计':'totalNonCurrentLiabilities',
        '负债合计':'totalLiabilities',
        '实收资本(或股本)':'totalShare',
        '资本公积':'capitalReserve',
        '盈余公积':'surplusReserve',
        '减:库存股':'treasuryStock',
        '未分配利润':'undistributedProfits',
        '少数股东权益':'minorityEquity',
        '外币报表折算差额':'foreignCurrenReportTransSpread',
        '所有者权益(或股东权益)合计':'totalOwnersEquity',
        '负债和所有者权益(或股东权益)总计':'totalLiabilitiesAnOwnersEquity',
        '营业收入':'operatingRevenue',
        '营业成本':'operatingCosts',
        '营业税金及附加':'taxAndSurcharges',
        '销售费用':'salesCosts',
        '管理费用':'managementCosts',
        '财务费用':'financialCosts',
        '资产减值损失':'assestsDevaluation',
        '公允价值变动收益':'profitLossFromFairValueChanges',
        '投资收益':'investmentIncome',
        '对联营企业和合营企业的投资收益':'invesIncomFrAffilBusiCooperEn',
        '营业利润':'operatingProfit',
        '补贴收入':'subsidyIncome',
        '营业外收入':'nonOperatingIncome',
        '营业外支出':'nonOperatingExpenses',
        '非流动资产处置损失':'netLossFrDisposOfNonCurrAssets',
        '利润总额':'totalProfit',
        '所得税费用':'incomeTax',
        '净利润':'netProfit',
        '归属于母公司所有者的净利润':'netProfitsBelToParComOwner',
        '少数股东损益':'minorityProfitAndLoss',
        '销售商品、提供劳务收到的现金':'cashFromGoodsSalOrRendOfServ',
        '收到的税费返还':'refundOfTaxAndFeeReceived',
        '收到的其他与经营活动有关的现金':'otherCashRelaBusiActivReceived',
        '经营活动现金流入小计':'cashInflowsFromOperatActiv',
        '购买商品、接受劳务支付的现金':'buyGoodsReceivCashPaidLabor',
        '支付给职工以及为职工支付的现金':'paymentToEmployCashPaidEmploy',
        '支付的各项税费':'paymentsOfVariousTaxes',
        '支付的其他与经营活动有关的现金':'payOfOtherCashRelatToBusiActiv',
        '经营活动现金流出小计':'cashOutOperaActiv',
        '经营活动产生的现金流量净额':'netCashOperatActiv',
        '收回投资所收到的现金':'cashReceivFromInvestRece',
        '取得投资收益所收到的现金':'cashReceivedFromInvestIncome',
        '处置固定资产、无形资产和其他长期资产所收回的现金净额':'dispCashLongTermAssets',
        '处置子公司及其他营业单位收到的现金净额':'dispNetCashReceivSubsBusiUnits',
        '收到的其他与投资活动有关的现金':'otherCashReceRelatInvestActiv',
        '投资活动现金流入小计':'cashinFlowsFromInvestActiv',
        '购建固定资产、无形资产和其他长期资产所支付的现金':'cashPayLongTermAssets',
        '投资所支付的现金':'cashInvestment',
        '取得子公司及其他营业单位支付的现金净额':'NetCashPaidBySubsBusiUnits',
        '支付的其他与投资活动有关的现金':'CashPaidRelatToInvestActiv',
        '投资活动现金流出小计':'cashOutInvestActiv',
        '投资活动产生的现金流量净额':'netCashFlowsFromInvestActiv',
        '吸收投资收到的现金':'cashReceivedFromInvestors',
        '取得借款收到的现金':'cashFromBorrowings',
        '收到其他与筹资活动有关的现金':'otherCashReceivRelatFinanActiv',
        '筹资活动现金流入小计':'cashInflowsFromFinanActiv',
        '偿还债务支付的现金':'cashPaymentsOfAmountBorrowed',
        '分配股利、利润或偿付利息所支付的现金':'cashPayDistDivProf',
        '支付其他与筹资活动有关的现金':'otherCashPayRelatToFinanActiv',
        '筹资活动现金流出小计':'cashOutflowsFromFinanActiv',
        '筹资活动产生的现金流量净额':'netCashFlowsFromFinanActiv',
        '汇率变动对现金及现金等价物的影响':'effOfForeExchRateChangesOnCash',
        '现金及现金等价物净增加额':'netIncCashCashEquiv',
        '加:期初现金及现金等价物余额':'initialCashAndCashEquivBalan',
        '期末现金及现金等价物余额':'theFinalCashAndCashEquivBalan',
        '净利润C':'netProfitFromOperatActiv',
        '资产减值准备':'provisionForAssetsLosses',
        '固定资产折旧、油气资产折耗、生产性物资折旧':'deprecForFixedAssets',
        '无形资产摊销':'amortizationOfIntangibleAssets',
        '长期待摊费用摊销':'cLongtermDeferredExpenses',
        '处置固定资产、无形资产和其他长期资产的损失':'lossDispLongtermAssets',
        '固定资产报废损失':'scrapLossOfFixedAssets',
        '公允价值变动损失':'lossFromFairValueChange',
        '财务费用C':'financialExpenses',
        '投资损失':'investmentLosses',
        '递延所得税资产减少':'decreaseOfDeferredTaxAssets',
        '递延所得税负债增加':'incrOfDeferredTaxLiabilities',
        '存货的减少':'decreaseOfInventory',
        '经营性应收项目的减少':'decreaseOfOperationReceivables',
        '经营性应付项目的增加':'increaseOfOperationPayables',
        '其他':'others',
        '债务转为资本':'debtConvertedToCSapital',
        '一年内到期的可转换公司债券':'convertibleBondMaturityOneYear',
        '融资租入固定资产':'leaseholdImprovements',
        '现金的期末余额':'cashEndingBal',
        '现金的期初余额':'cashBeginingBal',
        '现金等价物的期末余额':'cashEquivalentsEndingBal',
        '现金等价物的期初余额':'cashEquivalentsBeginningBal',
        'crawl_date':'crawl_date',
        'code':'code',
        'report_date':'report_date'
        }