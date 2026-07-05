import pandas as pd
import yfinance as yf


def get_intraday(ticker):
    try:
        df = yf.Ticker(ticker).history(interval="5m", period="1d")
        if df.empty:
            return None
        return df
    except:
        return None


def get_prev_high(ticker):
    df = yf.Ticker(ticker).history(period="5d")
    if df.empty:
        return None
    return df["High"].iloc[-2]  # kemarin


def calc_intraday_score(ticker):
    df = get_intraday(ticker)
    if df is None or df.empty:
        return 0

    try:
        last = df.iloc[-1]
        first = df.iloc[0]

        open_price = first["Open"]
        close = last["Close"]
        volume = df["Volume"].sum()

        # Momentum
        momentum = (close - open_price) / open_price

        # RVOL sederhana (vs rata-rata volume 5 candle awal)
        avg_vol = df["Volume"].mean()
        rvol = volume / avg_vol if avg_vol != 0 else 0

        # Breakout
        prev_high = get_prev_high(ticker)
        breakout = 1 if close > prev_high else 0

        # Range strength
        high = df["High"].max()
        low = df["Low"].min()
        range_strength = (high - low) / open_price

        score = (
            momentum * 40 +
            rvol * 30 +
            breakout * 20 +
            range_strength * 10
        )

        return score

    except:
        return 0


def rank_top10(tickers):
    results = []

    for t in tickers:
        score = calc_intraday_score(t)

        results.append({
            "ticker": t,
            "score": score
        })

    df = pd.DataFrame(results)
    df = df.sort_values(by="score", ascending=False)

    return df.head(10)