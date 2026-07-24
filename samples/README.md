# OptionVault Dataset Samples

This directory contains lightweight, raw CSV samples representing the structure and schemas of the data categories in OptionVault.

## Directory Structure

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
For detailed column descriptions, refer to the [data_dictionary.md](../docs/data_dictionary.md) in the `docs` folder.
