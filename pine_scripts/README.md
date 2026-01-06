# Rising Trend Line Strategy

This Pine Script implements an intraday strategy that identifies rising trend lines and enters long positions when the price interacts with the trend. It includes a configurable risk/reward ratio for managing trades.

## How to Use

1.  Open a chart on TradingView.
2.  Open the Pine Editor from the bottom panel.
3.  Copy the contents of `rising_trend_line_strategy.pine` and paste them into the editor.
4.  Click "Add to Chart" to apply the strategy.

## Inputs

*   **Risk/Reward Ratio:** Determines the take-profit level relative to the stop-loss. For example, a value of 2.0 sets the take-profit at twice the distance of the stop-loss from the entry price.
*   **Lookback Period for Swings:** The number of bars to look back to identify swing lows. These swings are used to draw the trend lines.
*   **Proximity Zone (%):** A percentage-based zone above the trend line. A trade can be initiated if the price enters this zone, allowing for more trades than a strict touch of the trend line.
