import pandas as pd
import sys
import os
import datetime

# Add the project root to the python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai_data_science_team.agents import financial_markets_agent

def create_bull_flag_data():
    """Creates a sample dataframe with a bull flag pattern."""
    data = {
        'Open':  [101, 105, 108, 112, 116, 119, 118, 117, 116, 117, 116, 115, 116, 117, 116, 115, 114, 115, 116, 115],
        'High':  [105, 108, 112, 116, 120, 120, 119, 118, 117, 118, 117, 116, 117, 118, 117, 116, 115, 116, 117, 116],
        'Low':   [100, 104, 107, 111, 115, 118, 117, 116, 115, 116, 115, 114, 115, 116, 115, 114, 113, 114, 115, 114],
        'Close': [105, 108, 112, 116, 120, 118, 117, 116, 117, 116, 115, 116, 117, 116, 115, 114, 115, 116, 115, 114],
        'ATRr_14': [5] * 20
    }
    dates = pd.to_datetime([datetime.date.today() - datetime.timedelta(days=19-i) for i in range(20)])
    df = pd.DataFrame(data, index=dates)
    return df

def create_no_bull_flag_data():
    """Creates a sample dataframe without a bull flag pattern."""
    data = {
        'Open':  [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119],
        'High':  [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
        'Low':   [99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118],
        'Close': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
        'ATRr_14': [1] * 20
    }
    dates = pd.to_datetime([datetime.date.today() - datetime.timedelta(days=19-i) for i in range(20)])
    df = pd.DataFrame(data, index=dates)
    return df

def test_bull_flag_detection():
    """Tests the bull flag detection algorithm."""
    print("Testing with bull flag data...")
    bull_flag_data = create_bull_flag_data()
    result = financial_markets_agent.detect_bull_flag(bull_flag_data)
    print(f"Result: {result}")
    assert result["signal"] == "BUY"

    print("\nTesting with no bull flag data...")
    no_bull_flag_data = create_no_bull_flag_data()
    result = financial_markets_agent.detect_bull_flag(no_bull_flag_data)
    print(f"Result: {result}")
    assert result["signal"] == "NONE"

if __name__ == "__main__":
    test_bull_flag_detection()
    print("\nAll tests passed!")
