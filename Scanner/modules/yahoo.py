import yfinance as yf
import pandas as pd
import time


def get_daily_data(ticker, period="1mo"):
    """
    Ambil data harian dari Yahoo Finance
    """
    try:
        data = yf.Ticker(ticker).history(period=period)
        if data.empty:
            return None
        return data
    except Exception as e:
        print(f"[ERROR] {ticker} daily data: {e}")
        return None


def get_intraday_data(ticker, interval="5m", period="1d"):
    """
    Ambil data intraday
    """
    try:
        data = yf.Ticker(ticker).history(interval=interval, period=period)
        if data.empty:
            return None
        return data
    except Exception as e:
        print(f"[ERROR] {ticker} intraday data: {e}")
        return None


def load_tickers(path="data/idx.csv"):
    """
    Baca daftar ticker IDX
    """
    try:
        df = pd.read_csv(path)
        if "Ticker" in df.columns:
            return df["Ticker"].dropna().tolist()
        return df.iloc[:, 0].dropna().tolist()
    except Exception as e:
        print(f"[ERROR] load tickers: {e}")
        return []


def batch_get_daily(tickers, sleep=0.2):
    """
    Ambil data banyak saham (lebih stabil)
    """
    results = {}

    for t in tickers:
        data = get_daily_data(t)
        if data is not None:
            results[t] = data
        time.sleep(sleep)

    return results