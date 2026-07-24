# Cash (SPOT) Samples

This folder contains 1-minute OHLCV (Open, High, Low, Close, Volume) bar data for the cash equity/spot segment.

## Files
- `ACC.csv`
- `RELIANCE.csv`
- `TCS.csv`
- `NIFTY50.csv`

## Schema
- `datetime`: Timestamp of the bar (1-minute resolution).
- `name`: Ticker/asset symbol name.
- `open`: Opening price of the bar.
- `high`: Highest price traded during the minute.
- `low`: Lowest price traded during the minute.
- `close`: Closing price of the bar.
- `volume`: Total traded volume.
- `oi`: Open Interest (always 0 for cash/spot segment).
