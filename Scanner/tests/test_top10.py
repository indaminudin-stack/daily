import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.selector import rank_top50
from modules.yahoo import load_tickers, batch_get_daily
from modules.intraday import rank_top10

tickers = load_tickers()

print("Loading Top 50 base...")

data = batch_get_daily(tickers[:30])

top50_df = rank_top50(data)

top50_list = top50_df["ticker"].tolist()

print("Calculating intraday Top 10...")

top10 = rank_top10(top50_list)

print(top10)