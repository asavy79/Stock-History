import numpy
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta


stock = input("Enter a stock ticker: ").upper()


ticker = yf.Ticker(stock)
startDate = (datetime.today() - timedelta(365)).strftime("%Y-%m-%d")
requestedPercentageIncrease = float(
    input("Enter a percentage increase you wish to look for as a decimal: "))

today = (datetime.today() + timedelta(1)).strftime("%Y-%m-%d")

history = ticker.history(start=startDate, end=today)["Close"]

dateList = history.keys().strftime("%Y-%m-%d")


requestTrue = 0
for i in range(1, len(dateList)):
    percentageIncrease = (history[dateList[i]] / history[dateList[i - 1]]) - 1
    if percentageIncrease > requestedPercentageIncrease:
        requestTrue = 1
        print(
            f"{stock} jumped {round(percentageIncrease * 100, 2)}% to {round(history[dateList[i]], 2)} on {dateList[i]}")

if not requestTrue:
    print(f"{stock} did not go up by {round(requestedPercentageIncrease * 100, 2)}% in a day from {startDate} to {today}")

print(startDate)
