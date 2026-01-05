import datetime
from ai_data_science_team.agents import financial_markets_agent

# Fetch data for a stock
ticker = "AAPL"
start_date = datetime.date.today() - datetime.timedelta(days=365)
end_date = datetime.date.today()
data = financial_markets_agent.get_stock_data(ticker, start_date, end_date)

# Detect bull flags
signals = financial_markets_agent.detect_bull_flag(data)

# Print signals
if signals:
    print(f"Found {len(signals)} bull flag signals for {ticker}:")
    for signal in signals:
        print(signal)
else:
    print(f"No bull flag signals found for {ticker}.")
