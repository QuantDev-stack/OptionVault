# Dataset Coverage

OptionVault contains comprehensive historical market data for the Indian financial markets (NSE, BSE, MCX). This document outlines the asset coverage, historical depth, and data granularities available in the full vault.

## 1. Asset Classes & Instruments

### Equity Index Derivatives (NFO)
- **NIFTY 50 Index Options & Futures**
- **BANKNIFTY Index Options & Futures**
- **FINNIFTY Index Options & Futures**
- **MIDCPNIFTY Index Options & Futures**

### Equity Stock Derivatives (NFO)
- Futures and Options contracts for all F&O-eligible underlying stocks (e.g. `RELIANCE`, `TCS`, `INFY`, `HDFCBANK`, `ACC`, `SBIN`).

### Index Spot Segment (NSE/BSE)
- Index Spot levels for `NIFTY50`, `BANKNIFTY`, `SENSEX`, and `BSE100`.

### Cash Equity Spot Segment (NSE)
- All liquid cash segment equities traded on the National Stock Exchange.

### Commodity Derivatives (MCX)
- Futures and Options for base metals, energy, and precious metals (`COPPER`, `CRUDEOIL`, `CRUDEOILM`, `GOLD`, `GOLDM`, `NATURALGAS`, `SILVER`, `SILVERM`, `ZINC`).

---

## 2. Historical Depth & Resolution

| Segment | Resolution | History Start | Coverage Completeness |
|---|---|---|---|
| Index Spot | 1-Second / 1-Minute | Jan 2018 | 99.9% |
| Cash Equity | 1-Minute OHLCV | Jan 2018 | 99.8% |
| Index Futures | 1-Minute OHLCV | Jan 2018 | 99.9% |
| Stock Futures | 1-Minute OHLCV | Jan 2018 | 99.7% |
| Index Options | Tick-by-Tick / 1-Sec | Jan 2020 | 99.5% |
| Index Options | 1-Minute OHLCV | Jan 2018 | 99.6% |
| Stock Options | 1-Minute OHLCV | Jan 2018 | 99.2% |
| Order Book L2 | 100ms snapshots | Jan 2023 | 99.0% |
| MCX Commodities | 1-Minute OHLCV | Jan 2020 | 98.9% |

---

## 3. Data Partitions & Storage Layout

The full OptionVault database is stored in high-performance **Apache Parquet** format on the storage nodes (`H:\DATA_V2` and `H:\TICK_DATA`), partitioned as follows:

```
H:/DATA_V2/
└── <SYMBOL>/                  # e.g., RELIANCE, NIFTY
    └── <YYYY-MM-DD>/          # Date partition
        ├── SPOT/
        │   └── <SYMBOL>_<YYYY-MM-DD>_SPOT.parquet
        ├── FUTURES/
        │   └── <SYMBOL>_<YYYY-MM-DD>_FUT.parquet
        └── OPTIONS/
            └── <SYMBOL>_<YYYY-MM-DD>_OPT.parquet
```

This layout allows query engines (DuckDB, Spark, Polars) to perform high-speed parallel scans using partition pruning.
