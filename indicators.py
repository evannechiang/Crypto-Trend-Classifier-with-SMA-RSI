import pandas as pd

def calculate_sma(df, window=14):
    df[f"SMA_{window}"] = df["price"].rolling(window=window).mean()
    return df

def calculate_ema(df, span=14):
    df[f"EMA_{span}"] = df["price"].ewm(span=span, adjust=False).mean()
    return df

def calculate_rsi(df, window=14):
    delta = df["price"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    df[f"RSI_{window}"] = 100 - (100 / (1 + rs))
    return df
