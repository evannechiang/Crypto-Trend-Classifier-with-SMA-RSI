import matplotlib.pyplot as plt

def plot_price_with_indicators(df, trend_label=None):
    plt.figure(figsize=(12, 6))

    # Plot price and indicators
    plt.plot(df.index, df["price"], label="Price", linewidth=2)

    if "SMA_14" in df.columns:
        plt.plot(df.index, df["SMA_14"], label="SMA 14", linestyle="--")
    if "EMA_14" in df.columns:
        plt.plot(df.index, df["EMA_14"], label="EMA 14", linestyle=":")

    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    title = "Bitcoin Price with Indicators"
    if trend_label:
        title += f" - Trend: {trend_label}"
    plt.title(title)

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

