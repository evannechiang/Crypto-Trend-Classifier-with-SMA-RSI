from fetch_data import fetch_bitcoin_price
from indicators import calculate_sma, calculate_ema, calculate_rsi
from trend_classifier import classify_trend
from plot_trends import plot_price_with_indicators

def main():
    # Step 1: Fetch BTC data for the past 90 days
    df = fetch_bitcoin_price(days=90, interval="daily")

    # Step 2: Calculate technical indicators
    df = calculate_sma(df, window=14)
    df = calculate_sma(df, window=50)     # Needed for SMA crossover
    df = calculate_ema(df, span=14)
    df = calculate_rsi(df, window=14)

    # Step 3: Classify trend using SMA crossover
    trend_signal = classify_trend(df)
    print("📈 Market Trend:", trend_signal)

    # Step 4: Plot the price and indicators
    plot_price_with_indicators(df, trend_label=trend_signal)

    # Optional: Save output
    df.to_csv("btc_trend_data.csv")
    print("✅ Data saved to btc_trend_data.csv")

if __name__ == "__main__":
    main()
