# How to Use the Pine Script Wedge Pattern Strategy

1.  **Copy the Script:** Open the `pine_scripts/wedge_pattern_strategy.pine` file and copy the entire contents of the script.
2.  **Open TradingView:** Navigate to [https://www.tradingview.com/](https://www.tradingview.com/) and open a chart.
3.  **Open the Pine Editor:** At the bottom of the TradingView chart, click on the "Pine Editor" tab.
4.  **Paste the Script:** Paste the script you copied into the Pine Editor.
5.  **Add to Chart:** Click the "Add to Chart" button in the Pine Editor.
6.  **View Backtesting Results:** Since this is a `strategy`, you can view the backtesting results in the "Strategy Tester" tab at the bottom of the chart.

## Configuration

You can configure the strategy's settings by clicking the gear icon next to the strategy's name on the chart.

### Confirmation Filters

*   **Enable Trend Filter:** When enabled, the strategy will only enter long trades if the price is above the EMA and short trades if it's below. This helps to ensure that you are trading with the overall trend.
*   **EMA Length:** Sets the lookback period for the Exponential Moving Average used in the trend filter.
*   **Enable Volume Filter:** When enabled, a breakout will only be considered valid if the volume on the breakout candle is significantly higher than the recent average volume. This helps to confirm that the breakout has strong momentum.
*   **Volume Factor:** Sets the multiplier for the average volume. For example, a factor of 1.5 means the breakout volume must be 150% of the average volume.
*   **Volume Lookback:** Sets the lookback period for calculating the average volume.
