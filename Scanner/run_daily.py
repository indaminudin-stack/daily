from modules.yahoo import load_tickers, batch_get_daily
from modules.selector import rank_top50
from modules.intraday import rank_top10
from modules.notifier import send_telegram

import os
TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]


def run_top50():
    tickers = load_tickers()
    data = batch_get_daily(tickers)
    top50 = rank_top50(data)
    top50.to_csv("data/top50.csv", index=False)

    msg = "📈 TOP 50 IDX\n\n"

    for i, row in top50.iterrows():
        msg += f"{i+1}. {row['ticker']} ({row['score']:.2f})\n"

    send_telegram(msg, TOKEN, CHAT_ID)


    print("Top 50 done")


def run_top10():
    import pandas as pd

    top50 = pd.read_csv("data/top50.csv")
    tickers = top50["ticker"].tolist()

    top10 = rank_top10(tickers)

    msg = "📈 TOP 10 IDX\n\n"

    for i, row in top10.iterrows():
        msg += f"{i+1}. {row['ticker']} ({row['score']:.2f})\n"

    send_telegram(msg, TOKEN, CHAT_ID)
    print("Top 10 sent")


if __name__ == "__main__":
    import sys

    mode = sys.argv[1] if len(sys.argv) > 1 else "top50"

    if mode == "top50":
        run_top50()
    elif mode == "top10":
        run_top10()


