import requests
import pandas as pd
from datetime import datetime

def fetch_bitcoin_price(days=30, interval="daily"):
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": interval  # 'daily' or 'hourly'
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("❌ Status Code:", response.status_code)
        print("❌ Response Text:", response.text)
        raise Exception("Failed to fetch data from CoinGecko")

    data = response.json()

    # Extract [timestamp, price]
    prices = data.get("prices", [])
    if not prices:
        raise Exception("No price data found in API response.")

    # Convert to DataFrame
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)

    return df

# Quick test
if __name__ == "__main__":
    try:
        df = fetch_bitcoin_price(days=30, interval="daily")
        print("✅ Data fetched successfully!")
        print(df.head())
    except Exception as e:
        print("❌ Error:", e)
