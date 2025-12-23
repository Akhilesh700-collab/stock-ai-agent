import yfinance as yf
import time
from datetime import datetime

STOCK_LIST = [
    "AAPL",    
    "MSFT",    
    "GOOGL",   
    "AMZN",   
    "TSLA",    
    "NVDA",    
    "META",    
    "NFLX",
    "FLIP",
    "JIO",
    "RELIANCE.NS",
    "TCS.NS", 
    "INFY.NS",
    "HDFCBANK.NS",

]

def fetch_and_analyze(symbol):
    try:
        data = yf.download(symbol, period="1d", interval="1d", progress=False)

        if data.empty:
            print(f"{symbol} → No data available")
            return

        open_price = float(data["Open"].iloc[-1])
        close_price = float(data["Close"].iloc[-1])
        high_price = float(data["High"].iloc[-1])
        low_price = float(data["Low"].iloc[-1])

        change = close_price - open_price
        percent = (change / open_price) * 100

        if close_price > open_price:
            trend = "Bullish "
        elif close_price < open_price:
            trend = "Bearish "
        else:
            trend = "Neutral "

        print("\n------------------------------")
        print("Stock:", symbol)
        print("Time:", datetime.now())
        print("Open:", round(open_price, 2))
        print("Close:", round(close_price, 2))
        print("High:", round(high_price, 2))
        print("Low:", round(low_price, 2))
        print("Change:", round(change, 2), f"({round(percent, 2)}%)")
        print("Trend:", trend)

    except Exception as e:
        print(f"Error processing {symbol}: {e}")

def run_auto_analysis():
    print("\n STOCK ANALYSIS AGENT STARTED ")

    while True:
        print("\n==============================")
        print("MARKET SCAN TIME:", datetime.now())
        print("==============================")

        for stock in STOCK_LIST:
            fetch_and_analyze(stock)

        print("\n⏳ Waiting for next cycle...\n")
        time.sleep(300)  

if __name__ == "__main__":
    run_auto_analysis()
