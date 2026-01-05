import yfinance as yf
import pandas as pd
import pandas_ta as ta
import numpy as np

def get_stock_data(ticker, start_date, end_date):
    """
    Fetches stock data for a given ticker, calculates technical indicators,
    and backfills any resulting NaN values.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    if not data.empty:
        # Calculate ATR and rolling average volume
        data.ta.atr(length=14, append=True)
        data['avg_volume'] = data['Volume'].rolling(window=20).mean()
        # Backfill NaNs that occur at the beginning of the series from indicator calculations
        data.bfill(inplace=True)
    return data

def detect_bull_flag(data, flagpole_bars=5, flag_bars=15, atr_multiplier=3.0, volume_multiplier=1.5):
    """
    Detects bull flag patterns in a given dataframe using volume, volatility,
    and trend analysis, with breakout confirmation.
    """
    signals = []
    if len(data) < flagpole_bars + flag_bars + 1:
        return signals

    # Iterate through the data to find patterns
    for i in range(len(data) - flagpole_bars - flag_bars - 1):
        flagpole_data = data.iloc[i : i + flagpole_bars]
        flag_data = data.iloc[i + flagpole_bars : i + flagpole_bars + flag_bars]

        # 1. Flagpole Detection
        flagpole_start_low = flagpole_data['Low'].min()
        flagpole_end_high = flagpole_data['High'].max()
        flagpole_height = flagpole_end_high - flagpole_start_low

        # Ensure data is valid before checking conditions
        if flagpole_data.empty or pd.isna(flagpole_data['ATRr_14'].iloc[-1]) or pd.isna(flagpole_data['avg_volume'].iloc[-1]):
            continue

        flagpole_volume_surge = flagpole_data['Volume'].max() > flagpole_data['avg_volume'].iloc[-1] * volume_multiplier
        flagpole_is_steep = flagpole_height > flagpole_data['ATRr_14'].iloc[-1] * atr_multiplier

        if not (flagpole_is_steep and flagpole_volume_surge):
            continue

        # 2. Flag Consolidation Detection
        flag_high = flag_data['High'].max()
        flag_low = flag_data['Low'].min()

        if flag_data.empty or pd.isna(flag_data['avg_volume'].iloc[-1]):
            continue

        flag_volume_declining = flag_data['Volume'].mean() < flag_data['avg_volume'].iloc[-1]

        # Use linear regression to confirm a slight downward or sideways trend
        x = np.arange(len(flag_data))
        y = flag_data['Close'].values
        slope, _ = np.polyfit(x, y, 1)

        # The consolidation range should be less than 50% of the flagpole's height
        is_consolidating = (flag_high - flag_low) < flagpole_height * 0.5

        if not (is_consolidating and flag_volume_declining and slope < 0):
            continue

        # 3. Breakout Confirmation
        breakout_candle = data.iloc[i + flagpole_bars + flag_bars]
        if breakout_candle['Close'] > flag_high:
            entry_price = flag_high
            stop_loss = flag_low
            # Ensure risk/reward is logical
            if (entry_price - stop_loss) <= 0:
                continue
            take_profit = entry_price + (entry_price - stop_loss) * 2 # 2:1 risk-reward ratio

            signals.append({
                "signal": "BUY",
                "date": breakout_candle.name,
                "entry_price": round(entry_price, 2),
                "stop_loss": round(stop_loss, 2),
                "take_profit": round(take_profit, 2)
            })

    return signals
