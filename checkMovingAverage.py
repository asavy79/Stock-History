import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time

stocks = [
    "AAPL", "GOOG", "NVDA", "MSFT", "AMZN", "TSLA", "META", "GOOGL", "BRK-B", "UNH", "HD",
    "XOM", "LLY", "JPM", "JNJ", "V", "PG", "MA", "AVGO", "HD", "MRK", "ABBV", "ADBE",
    "WMT", "PEP", "DIS", "COST", "CVX", "MCD", "CRM", "INTC", "PFE", "VZ", "TMO", "NFLX",
    "NEE", "BKNG", "KO", "LIN", "CAT", "NKE", "HON", "COST", "MS", "RTX", "WFC",
    "JXN", "DHR", "IBM", "DOW", "UPS", "MMM", "LOW", "BA", "LLY", "T", "UNM", "TJX",
    "LMT", "MDLZ", "MMM", "CHTR", "AMD", "AEP", "AON", "AIG", "APTV", "ACGL", "ANET",
    "AJG", "AIZ", "T", "ABT", "ACN", "ATVI", "ADSK", "ALGN", "ALL", "GOOGL", "GOOG",
    "ALLE", "MO", "AMAT", "ADM", "AEE", "AAL", "AEP", "AXP", "AIG", "AIZ", "AFL", "AMG",
    "ADI", "ADP", "AAP", "AES", "APA", "ARE", "ADM", "AON", "ATO", "ATUS", "ABBV", "AVGO",
    "BKR", "BBY", "BZH", "BA", "BAC", "BKNG", "BURL", "BXP", "C", "CAT", "CB", "CSCO",
    "CTLT", "CMG", "CHTR", "CVX", "CCL", "COST", "CCI", "DHR", "DOV", "DUK", "DXC", "EMR",
    "EMR", "EFX", "ECL", "EQT", "EIX", "EPD", "ETR", "EVRG", "EXPD", "EXPD", "FAST", "FDX",
    "FERG", "FIS", "FSLR", "FTI", "FLT", "FOX", "FOXA", "FTNT", "FTV", "GOOGL", "GOOG", "GILD",
    "GM", "GPC", "GRMN", "HAL", "HAS", "HCA", "HD", "HES", "HIG", "HLT", "HPE", "HUM", "IBM",
    "INTC", "ITW", "JPM", "JNJ", "JXN", "KMB", "KO", "KEY", "KR", "LIN", "LMT", "LOW",
    "LPX", "LRCX", "LYV", "MAA", "MAR", "MA", "MCD", "MDLZ", "MDT", "MET", "MGM", "MCHP",
    "MCK", "MDLZ", "MMM", "MS", "MSFT", "MU", "NEE", "NFLX", "NKE",
    "NVDA", "NVO", "NWL", "OXY", "ODFL", "OKTA", "ORCL", "PGR", "PG", "PNC", "PFE",
    "PRU", "PSX", "PYPL", "QCOM", "REGN", "RELX", "RMD", "ROK", "RCL", "ROL", "ROP", "RTX",
    "RYN", "SBUX", "SLB", "SCHW", "SRE", "SE", "SEE", "SHW", "SBNY", "SLG", "SMG", "SNA",
    "SO", "SOHU", "SPG", "SWK", "TGT", "TEL", "TER", "TSLA", "TMO", "TPR", "TROW",
    "TTWO", "TXN", "UHS", "UNH", "UPS", "USB", "V", "VRTX", "VZ", "WAB", "WBA", "LULU",
    "QQQ"

]


names = " ".join(stocks)

maValue1 = int(input("Enter shorter period moving average: "))
maValue2 = int(input("Enter longer period moving average: "))

startTime = time.time()

history = yf.download(tickers=names,
                      start=(datetime.now() - timedelta(160+maValue2)), end=datetime.now(), progress=False)["Close"]

for name in stocks:

    stockHistory = history[name]

    movingAverageHigher = list(stockHistory.rolling(maValue2).mean())
    movingAverageLower = list(stockHistory.rolling(maValue1).mean())
    dateList = stockHistory.keys().strftime("%Y-%m-%d")

    for i in range(0, len(dateList)):
        if not pd.isna(movingAverageLower[i]) and not pd.isna(movingAverageHigher[i]) and i != 0:
            if movingAverageLower[i-1] < movingAverageHigher[i-1] and movingAverageLower[i] > movingAverageHigher[i]:
                print(
                    f"{name}'s {maValue1}-day moving average crossed it's {maValue2}-day moving average on {dateList[i]}")

stopTime = time.time() - startTime

print(
    f"********** Process Completed in {round(stopTime, 2)} seconds **********")
