import pandas as pd
import math


def calculate_score(df):
    last = df.iloc[-1]

    open_ = last["Open"]
    close = last["Close"]
    high = last["High"]
    low = last["Low"]
    volume = last["Volume"]

    if open_ == 0:
        return 0

    return_pct = (close - open_) / open_
    range_pct = (high - low) / open_
    volume_score = math.log(volume + 1)
    price_factor = 1 / (close + 1)

    score = (
        return_pct * 50 +
        range_pct * 30 +
        volume_score * 10 +
        price_factor * 10
    )

    return score


def rank_top50(data_dict):
    results = []

    for ticker, df in data_dict.items():
        results.append({
            "ticker": ticker,
            "score": calculate_score(df),
            "volume": df.iloc[-1]["Volume"],
            "close": df.iloc[-1]["Close"]
        })

    df = pd.DataFrame(results)
    return df.sort_values("score", ascending=False).head(50)