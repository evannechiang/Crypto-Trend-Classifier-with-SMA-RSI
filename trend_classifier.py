import pandas as pd

def classify_trend(df):
    # Ensure both SMA columns are present
    if "SMA_14" not in df.columns or "SMA_50" not in df.columns:
        return "Missing SMA data"

    # Get the latest SMA values
    short_sma = df["SMA_14"].iloc[-1]
    long_sma = df["SMA_50"].iloc[-1]

    # Check for NaN (early rows of SMA_50 may be NaN)
    if pd.isna(short_sma) or pd.isna(long_sma):
        return "Not enough data"

    # Crossover logic
    if short_sma > long_sma:
        return "Bullish"
    elif short_sma < long_sma:
        return "Bearish"
    else:
        return "Neutral"
