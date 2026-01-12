import pandas as pd
import sys
import os
import datetime
import numpy as np
import pandas_ta as ta

# Add the project root to the python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai_data_science_team.agents import financial_markets_agent

def create_targeted_bull_flag_data():
    """Creates a targeted dataframe with a bull flag pattern."""
    # Base data
    dates = pd.to_datetime([datetime.date.today() - datetime.timedelta(days=49-i) for i in range(50)])
    base_prices = np.linspace(100, 105, 50)
    volume = np.full(50, 100000)

    # Flagpole (bars 10-14)
    base_prices[10:15] = [110, 115, 120, 125, 130]
    volume[10:15] = [200000, 250000, 300000, 350000, 400000]

    # Flag (bars 15-30)
    base_prices[15:30] = np.linspace(128, 125, 15)
    volume[15:30] = np.linspace(150000, 80000, 15)

    # Breakout (bar 30)
    base_prices[30] = 135
    volume[30] = 300000

    data = {
        'Open': base_prices - 1,
        'High': base_prices + 1,
        'Low': base_prices - 2,
        'Close': base_prices,
        'Volume': volume
    }
    df = pd.DataFrame(data, index=dates)
    return df

def test_bull_flag_detection():
    """Tests the bull flag detection algorithm with targeted data."""
    print("Testing with targeted bull flag data...")
    bull_flag_data = create_targeted_bull_flag_data()

    # Process data
    bull_flag_data.ta.atr(length=14, append=True)
    bull_flag_data['avg_volume'] = bull_flag_data['Volume'].rolling(window=20).mean()
    bull_flag_data.bfill(inplace=True)

    signals = financial_markets_agent.detect_bull_flag(bull_flag_data)
    print(f"Result: {signals}")
    assert len(signals) > 0
    assert signals[0]['signal'] == 'BUY'

if __name__ == "__main__":
    test_bull_flag_detection()
    print("\nAll tests passed!")
