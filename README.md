# OptionVault

Historical Indian financial market datasets for quantitative research, algorithmic trading, backtesting, and market microstructure analysis.

---

## Coverage
    
| Market | Coverage | Resolution | Data |
|---------|----------|------------|------|
| **NSE Cash** | 2018 – Present | 1 Minute | OHLCV |
| **NSE Index** | 2022 – Present | 1 Second | OHLC |
| **NSE Futures** | 2018 – Present | 1 Minute | OHLC, Volume, OI |
| **NSE Options** | 2018 – Present | 1 Minute | OHLC, Volume, OI, Greeks |
| **MCX Futures** | 2023 – Present | 1 Minute | OHLC, Volume, OI |
| **MCX Options** | 2023 – Present | 1 Minute | OHLC, Volume, OI, Greeks |
| **Tick Data** | Available | Tick-by-Tick | Trade Events |
| **Level 2** | Available | Snapshot | Market Depth |

---

# Dataset Schema

## Spot Data

| Column | Description |
|---------|-------------|
| datetime | Candle timestamp |
| open | Open price |
| high | High price |
| low | Low price |
| close | Close price |
| volume | Traded volume |
| oi | Open Interest (0 for Spot) |
| name | Underlying Name |
| symbol | Trading Symbol |
| exp | Expiry (placeholder for Spot) |
| strike | Strike (0 for Spot) |
| type | Instrument Type |
| partKey | Partition Key |

---

## Futures

| Column | Description |
|---------|-------------|
| datetime | Candle timestamp |
| open, high, low, close | OHLC |
| volume | Traded volume |
| oi | Open Interest |
| name | Underlying |
| symbol | Contract Symbol |
| expiry | Contract Expiry |
| contract_type | FUT |

---

## Options

### Market Data

| Column | Description |
|---------|-------------|
| datetime | Candle timestamp |
| open, high, low, close | OHLC |
| volume | Traded volume |
| oi | Open Interest |
| name | Underlying |
| symbol | Option Symbol |
| strike | Strike Price |
| expiry | Expiry Date |
| contract_type | OPT |
| side | CE / PE |

### Greeks

| First Order | Higher Order |
|-------------|--------------|
| IV | Vanna |
| Delta | Charm |
| Gamma | Vomma |
| Vega | Speed |
| Theta | Zomma |
| Rho | Color |
|  | Veta |
|  | Ultima |
|  | Dual Delta |
|  | Dual Gamma |

---

# Sample Files

```
samples/
├── cash/
│   ├── ACC.csv
│   ├── RELIANCE.csv
│   └── NIFTY50.csv
│
├── derivatives/
│   ├── futures/
│   │   └── NIFTY25JAN18FUT.csv
│   │
│   ├── options/
│   │   └── NIFTY23JUN2214000CE.csv
│   │
│   └── greeks/
│       └── NIFTY23JUN2214000CE.csv
│
├── index_1sec/
│   └── NIFTY50.csv
│
├── market_depth/
│   ├── tick_data/
│   │   ├── NIFTY_tick.csv
│   │   └── combined_indices_tick.csv
│   └── level2/
│       └── NIFTY_level2.csv
│
└── mcx/
    ├── futures/
    │   └── COPPER26JUNFUT.csv
    └── options/
        └── COPPER26JUN800CE.csv
```

---

# Designed For

| | | |
|---|---|---|
| Quantitative Research | Backtesting | Algorithmic Trading |
| Statistical Arbitrage | Machine Learning | Volatility Research |
| Portfolio Analytics | Execution Research | Market Microstructure |
| HFT Simulation | Liquidity Analysis | Risk Analytics |

---

# Repository Contents

- Sample datasets
- Dataset schema
- Data dictionary
- Column reference
- Example notebooks

---

# Dataset Availability

- **Total Dataset Size:** **300+ GB** of historical market data.
- **Google Drive Samples:** Access additional sample datasets directly on our [Google Drive Samples Folder](https://drive.google.com/drive/folders/1lkS5P3fzQ7C-RUBAG_qvbvihET1chTJ1?usp=sharing).
- **Cloud Access:** All licensed datasets are uploaded to Google Drive for fast and convenient access.
- **Organized Structure:** Data is organized by market, instrument, and date to simplify downloading and integration into research or trading pipelines.
- **Regular Updates:** Historical datasets are continuously expanded with new market data.

Note: Sample files in this repository are provided for evaluation purposes. The complete 300+ GB dataset is available to licensed users via Google Drive.

---

# Contact

| Platform | Details |
|----------|---------|
| GitHub | Open an Issue or Discussion |
| Telegram | https://t.me/QuantDevstack |

---

## Disclaimer

Sample datasets are provided for evaluation purposes only. Commercial datasets require licensing.
