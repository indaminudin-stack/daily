import yfinance as yf
ticker = yf.Ticker("BBCA.JK")
data = ticker.history(period="5d")
print(data)