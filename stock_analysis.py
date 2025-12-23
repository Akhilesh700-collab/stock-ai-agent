import yfinance as yf
from datetime import datetime

def fetch_stock_data(symbol="AAPL"):
    data = yf.download(symbol, period="1d", interval="1d")
    return data

def analyze_stock(data):
    open_price = float(data["Open"].iloc[-1])
    close_price = float(data["Close"].iloc[-1])
    high_price = float(data["High"].iloc[-1])
    low_price = float(data["Low"].iloc[-1])

    change = close_price - open_price
    percent_change = (change / open_price) * 100

    if close_price > open_price:
        trend = "Bullish "
    elif close_price < open_price:
        trend = "Bearish "
    else:
        trend = "Neutral "

    return {
        "open": round(open_price, 2),
        "close": round(close_price, 2),
        "high": round(high_price, 2),
        "low": round(low_price, 2),
        "change": round(change, 2),
        "percent": round(percent_change, 2),
        "trend": trend
    }

def print_report(symbol, result):
    print("\n==============================")
    print("AUTOMATED STOCK ANALYSIS REPORT")
    print("==============================")
    print("Time:", datetime.now())
    print("Stock:", symbol)
    print("Open Price:", result["open"])
    print("Close Price:", result["close"])
    print("High:", result["high"])
    print("Low:", result["low"])
    print("Price Change:", result["change"], f"({result['percent']}%)")
    print("Market Trend:", result["trend"])
    print("==============================\n")

def main():
    symbol = "AAPL"  # Change stock symbol if needed
    data = fetch_stock_data(symbol)
    result = analyze_stock(data)
    print_report(symbol, result)

if __name__ == "__main__":
    main()
