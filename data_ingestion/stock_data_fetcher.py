# Extraction

import pandas as pd
import yfinance as yf
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
data = yf.download(tickers, period="1y")
Data_columns=data[["Open", "High", "Low", "Close"]]
