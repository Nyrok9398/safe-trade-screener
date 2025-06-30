
import pandas as pd

def get_options_spreads():
    # Simulated options data for display
    data = [
        {"Ticker": "SPY", "Type": "CALL", "Short": 550, "Long": 555, "Credit": 1.1, "MaxLoss": 3.9, "PoP": 0.84, "Delta": 0.19, "Signal": "Bearish"},
        {"Ticker": "AAPL", "Type": "PUT", "Short": 180, "Long": 175, "Credit": 1.0, "MaxLoss": 4.0, "PoP": 0.88, "Delta": 0.15, "Signal": "Bullish"},
    ]
    return pd.DataFrame(data)
