import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.yahoo import load_tickers, batch_get_daily

tickers = load_tickers()

print("Total ticker:", len(tickers))

data = batch_get_daily(tickers[:5])  # test 5 saham dulu

for t, df in data.items():
    print("\n", t)
    print(df.tail())