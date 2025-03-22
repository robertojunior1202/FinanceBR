import pandas as pd
import pandas_datareader.data as web
from yahoo_fin import stock_info as si
import datetime
import yfinance as yf


keys = [['address1', 'address2', 'city', 'state', 'zip', 'country', 'phone', 'website', 'industry', 'industryKey', 'industryDisp', 
         'sector', 'sectorKey', 'sectorDisp', 'longBusinessSummary', 'companyOfficers', 'auditRisk', 'boardRisk', 'compensationRisk', 
         'shareHolderRightsRisk', 'overallRisk', 'governanceEpochDate', 'maxAge', 'priceHint', 'previousClose', 'open', 'dayLow', 
         'dayHigh', 'regularMarketPreviousClose', 'regularMarketOpen', 'regularMarketDayLow', 'regularMarketDayHigh', 'dividendRate', 
         'dividendYield', 'exDividendDate', 'payoutRatio', 'fiveYearAvgDividendYield', 'beta', 'trailingPE', 'forwardPE', 'volume', 
         'regularMarketVolume', 'averageVolume', 'averageVolume10days', 'averageDailyVolume10Day', 'bid', 'ask', 'marketCap', 
         'fiftyTwoWeekLow', 'fiftyTwoWeekHigh', 'priceToSalesTrailing12Months', 'fiftyDayAverage', 'twoHundredDayAverage', 
         'trailingAnnualDividendRate', 'trailingAnnualDividendYield', 'currency', 'enterpriseValue', 'profitMargins', 'floatShares', 
         'sharesOutstanding', 'heldPercentInsiders', 'heldPercentInstitutions', 'impliedSharesOutstanding', 'bookValue', 'priceToBook', 
         'lastFiscalYearEnd', 'nextFiscalYearEnd', 'mostRecentQuarter', 'earningsQuarterlyGrowth', 'netIncomeToCommon', 'trailingEps', 
         'forwardEps', 'lastSplitFactor', 'lastSplitDate', 'enterpriseToRevenue', 'enterpriseToEbitda', '52WeekChange', 
         'SandP52WeekChange', 'lastDividendValue', 'lastDividendDate', 'exchange', 'quoteType', 'symbol', 'underlyingSymbol', 
         'shortName', 'longName', 'firstTradeDateEpochUtc', 'timeZoneFullName', 'timeZoneShortName', 'uuid', 'messageBoardId', 
         'gmtOffSetMilliseconds', 'currentPrice', 'targetHighPrice', 'targetLowPrice', 'targetMeanPrice', 'targetMedianPrice', 
         'recommendationMean', 'recommendationKey', 'numberOfAnalystOpinions', 'totalCash', 'totalCashPerShare', 'ebitda', 'totalDebt', 
         'quickRatio', 'currentRatio', 'totalRevenue', 'debtToEquity', 'revenuePerShare', 'returnOnAssets', 'returnOnEquity', 
         'freeCashflow', 'operatingCashflow', 'earningsGrowth', 'revenueGrowth', 'grossMargins', 'ebitdaMargins', 'operatingMargins', 
         'financialCurrency', 'trailingPegRatio']]

acoes = ["ITSA4.SA","BBAS3.SA","PETR4.SA","ITUB3.SA","BRAP4.SA"]



def dadosAcoes(start_date, end_date,*args, **kwargs):
   
    for item in args:
        try:
            info = yf.Ticker(item).info
            valores = si.get_data(item, start_date=start_date, end_date=end_date)
            print(f"Ação: {item} - {info['longName']} - {valores}")
            
        except:
            print(f"Ação: {item} - Sem alguma Info")
    
    
dadosAcoes("2024-12-12","2024-12-14",*acoes)

#dados[['open', 'close']]
#acao = yf.Ticker(**kwargs)
    #info = acao.info["longName"]
    #print(info)
    

