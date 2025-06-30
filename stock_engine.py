
import yfinance as yf
import pandas as pd
import pandas_ta as ta

def get_stock_signals():
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "JPM", "V", "UNH"]
    results = []
    for ticker in tickers:
        try:
            df = yf.download(ticker, period="90d", interval="1d")
            if df.empty or len(df) < 20:
                continue
            close = df["Close"]
            rsi = ta.rsi(close).iloc[-1]
            sma = ta.sma(close).iloc[-1]
            macd = ta.macd(close)["MACD_12_26_9"].iloc[-1]
            signal = "LONG" if rsi < 40 and macd > 0 and close.iloc[-1] < sma else                      "SHORT" if rsi > 60 and macd < 0 and close.iloc[-1] > sma else "NEUTRAL"
            score = sum([rsi < 40, macd > 0, close.iloc[-1] < sma])
            results.append({
                "Ticker": ticker,
                "Price": round(close.iloc[-1], 2),
                "RSI": round(rsi, 2),
                "MACD": round(macd, 4),
                "SMA": round(sma, 2),
                "Score": score,
                "Signal": signal
            })
        except:
            continue
    return pd.DataFrame(results).sort_values(by="Score", ascending=False).reset_index(drop=True)
