import pandas as pd

def classify_trend(df):
    if "SMA_14" not in df.columns or "SMA_50" not in df.columns:
        return "Missing SMA data"

    short_sma = df["SMA_14"].iloc[-1]
    long_sma = df["SMA_50"].iloc[-1]

    if pd.isna(short_sma) or pd.isna(long_sma):
        return "Not enough data"

    if short_sma > long_sma:
        return "Bullish"
    elif short_sma < long_sma:
        return "Bearish"
    else:
        return "Neutral"
