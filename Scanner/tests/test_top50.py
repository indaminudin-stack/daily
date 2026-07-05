import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.yahoo import load_tickers, batch_get_daily
from modules.selector import rank_top50

tickers = load_tickers()

print("Loading data...")

data = batch_get_daily(tickers[:30])  # test dulu 30 saham

top50 = rank_top50(data)

print(top50)