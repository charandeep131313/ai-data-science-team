# Pine Script Usage Instructions

This document provides instructions on how to use the custom Pine Script indicators in your TradingView charts.

## Bull Flag Indicator

The `bull_flag_indicator.pine` script is designed to detect bull flag patterns on your chart.

### How to Use

1.  **Copy the Script Code**:
    *   Open the file `pine_scripts/bull_flag_indicator.pine`.
    *   Select and copy the entire content of the file.

2.  **Open TradingView**:
    *   Navigate to [TradingView](https://www.tradingview.com/) and open a chart for any financial instrument.

3.  **Open Pine Editor**:
    *   At the bottom of the chart, click on the **Pine Editor** tab. This will open a code editor panel.

4.  **Paste the Code**:
    *   In the Pine Editor, delete any existing template code.
    *   Paste the code you copied from the `bull_flag_indicator.pine` file.

5.  **Add to Chart**:
    *   Click the **"Add to Chart"** button located above the Pine Editor. The script will be compiled and applied to your chart.

6.  **View the Signals**:
    *   The script will now run on your chart. When a bull flag pattern is detected, a green "Bull Flag" label will appear below the corresponding bar.

### Customization

You can customize the indicator's parameters by clicking the **Settings** icon next to the indicator's name on your chart. The following options are available:

*   **ATR Length**: The lookback period for the Average True Range (ATR) calculation.
*   **Flagpole Bars**: The number of bars to consider for the flagpole.
*   **Flag Bars**: The number of bars to consider for the flag.
*   **ATR Multiplier**: The multiplier used to determine the steepness of the flagpole.
*   **Risk/Reward Ratio**: The desired risk-to-reward ratio for trade signals.
