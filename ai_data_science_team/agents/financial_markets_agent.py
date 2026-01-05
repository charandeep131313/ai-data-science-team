import yfinance as yf
import pandas as pd
import pandas_ta as ta

def get_stock_data(ticker, start_date, end_date):
    """
    Fetches stock data for a given ticker.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    if not data.empty:
        data.ta.atr(append=True)
    return data

def detect_bull_flag(data):
    """
    Detects a bull flag pattern in the given data.
    """
    if len(data) < 20:
        return {"signal": "NONE"}

    candlesticks = data.tail(20).copy() # Look at the last 20 candles

    # Flagpole
    flagpole_candlesticks = candlesticks.iloc[:5]
    flagpole_start = flagpole_candlesticks['Low'].iloc[0]
    flagpole_end = flagpole_candlesticks['High'].iloc[-1]
    flagpole_height = flagpole_end - flagpole_start

    # Flag
    flag_candlesticks = candlesticks.iloc[5:]
    flag_high = flag_candlesticks['High'].max()
    flag_low = flag_candlesticks['Low'].min()

    # Conditions
    atr_col = 'ATRr_14'
    # Handle potential MultiIndex in columns from yfinance when multiple tickers are fetched
    if isinstance(candlesticks.columns, pd.MultiIndex):
        # Assuming the structure is (Value, Ticker), we need to select the ATR for the specific ticker
        # This part might need adjustment depending on the exact MultiIndex structure
        # For simplicity, this example assumes a single ticker is processed at a time in this function.
        # If the app supports multiple tickers, this logic needs to be more robust.
        atr_values = candlesticks.xs(atr_col, level=0, axis=1)
        atr_series = atr_values.iloc[:, 0] # Take the first ticker's ATR
    else:
        atr_series = candlesticks[atr_col]

    if atr_series.empty or pd.isna(atr_series.iloc[-1]):
        return {"signal": "NONE", "reason": "ATR not available"}

    flagpole_is_steep = flagpole_height > atr_series.iloc[-1] * 3
    flag_is_consolidating = (flag_high - flag_low) < flagpole_height * 0.5
    flag_is_downtrend = flag_candlesticks['Close'].iloc[-1] < flag_candlesticks['Open'].iloc[0]

    if flagpole_is_steep and flag_is_consolidating and flag_is_downtrend:
        # Buy signal
        entry_price = flag_high
        stop_loss = flag_low
        take_profit = entry_price + (entry_price - stop_loss) * 2 # 2:1 risk-reward ratio

        return {
            "signal": "BUY",
            "entry_price": entry_price,
            "stop_loss": stop_loss,
            "take_profit": take_profit
        }
    else:
        return {"signal": "NONE"}
