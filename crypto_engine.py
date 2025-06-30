import numpy as np
NaN = np.nan
import requests
import pandas as pd
import pandas_ta as ta

def get_crypto_signals():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10, "page": 1}
    coins = requests.get(url, params=params).json()

    results = []
    for coin in coins:
        try:
            df = requests.get(f"https://api.coingecko.com/api/v3/coins/{coin['id']}/ohlc?vs_currency=usd&days=90").json()
            df = pd.DataFrame(df, columns=["time", "open", "high", "low", "close"])
            if len(df) < 20:
                continue
            close_prices = pd.Series(df["close"].values)
            rsi = ta.rsi(close_prices).iloc[-1]
            sma = ta.sma(close_prices).iloc[-1]
            macd = ta.macd(close_prices)["MACD_12_26_9"].iloc[-1]
            signal = "LONG" if rsi < 40 and macd > 0 and close_prices.iloc[-1] < sma else                      "SHORT" if rsi > 60 and macd < 0 and close_prices.iloc[-1] > sma else "NEUTRAL"
            score = sum([rsi < 40, macd > 0, close_prices.iloc[-1] < sma])
            results.append({
                "Symbol": coin["symbol"].upper(),
                "Name": coin["name"],
                "Price": coin["current_price"],
                "RSI": round(rsi, 2),
                "MACD": round(macd, 4),
                "SMA": round(sma, 2),
                "Score": score,
                "Signal": signal
            })
        except:
            continue
    return pd.DataFrame(results).sort_values(by="Score", ascending=False).reset_index(drop=True)
