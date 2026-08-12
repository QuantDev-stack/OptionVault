# Data Dictionary

This document defines the schema columns, data types, and business meanings for all files in OptionVault.

## 1. Cash (SPOT) & Futures Schema

| Column Name | Data Type | Description |
|---|---|---|
| `datetime` | `timestamp[ns]` | Timestamp of the bar (exchange time, local timezone IST). |
| `name` | `string` | Base asset name (e.g. `RELIANCE`, `NIFTY50`). |
| `symbol` | `string` | Unique trading symbol contract (Futures only, e.g. `NIFTY25JAN18FUT`). |
| `open` | `double` | Opening price of the bar. |
| `high` | `double` | Highest price traded during the bar interval. |
| `low` | `double` | Lowest price traded during the bar interval. |
| `close` | `double` | Closing price of the bar. |
| `volume` | `int64` | Total traded contract/share quantity. |
| `oi` | `int64` | Open Interest (total active contracts outstanding). |
| `expiry` | `date` | Contract expiry date (`YYYY-MM-DD`). |
| `contract_type`| `string` | Instrument type identifier (`FUT`). |

---

## 2. Options Segment Schema

| Column Name | Data Type | Description |
|---|---|---|
| `datetime` | `timestamp[ns]` | Timestamp of the bar. |
| `name` | `string` | Underlying asset name (e.g. `NIFTY`). |
| `symbol` | `string` | Full option contract symbol (e.g., `NIFTY23JUN2214000CE`). |
| `open` | `double` | Opening option premium. |
| `high` | `double` | Highest option premium. |
| `low` | `double` | Lowest option premium. |
| `close` | `double` | Closing option premium. |
| `volume` | `int64` | Traded volume. |
| `oi` | `int64` | Open Interest. |
| `strike` | `double` | Option strike price. |
| `expiry` | `date` | Expiry date of the contract. |
| `side` / `contract_type` | `string` | Call (`CE`) or Put (`PE`). |

---

## 3. Option Greeks Fields

Option files in the `greeks/` directory contain additional calculated columns:

| Column Name | Data Type | Description |
|---|---|---|
| `iv` | `double` | Annualized Implied Volatility (in percentage, e.g. `14.5` = 14.50%). |
| `delta` | `double` | Option Delta ($\Delta$) — price sensitivity to underlying change. |
| `gamma` | `double` | Option Gamma ($\Gamma$) — acceleration rate of Delta. |
| `vega` | `double` | Option Vega ($\nu$) — sensitivity to 1% change in IV. |
| `theta` | `double` | Option Theta ($\theta$) — time decay per day. |
| `rho` | `double` | Option Rho ($\rho$) — interest rate sensitivity. |
| `vanna` | `double` | Second-order Greek: change in Delta per 1% change in volatility. |
| `charm` | `double` | Second-order Greek: change in Delta per day (time-decay of Delta). |
| `vomma` | `double` | Second-order Greek: sensitivity of Vega to changes in volatility. |
| `speed` | `double` | Third-order Greek: change in Gamma per underlying price change. |
| `zomma` | `double` | Third-order Greek: change in Gamma per 1% change in volatility. |
| `color` | `double` | Third-order Greek: change in Gamma per day (time-decay of Gamma). |
| `veta` | `double` | Second-order Greek: change in Vega per day. |
| `ultima` | `double` | Third-order Greek: sensitivity of Vomma to volatility. |

---

## 4. Tick-Level Schema

| Column Name | Data Type | Description |
|---|---|---|
| `timestamp` | `timestamp[us]` | Precise microsecond timestamp of transaction event. |
| `price` | `double` | Transaction execution price. |
| `volume` | `int64` | Cumulative volume traded. |
| `tradingsymbol`| `string` | Full contract symbol name. |
| `instrument_type`| `string` | Instrument class (`OPT`, `FUT`, `EQ`). |
| `expiry` | `date` | Contract expiry. |
| `strike` | `double` | Strike price (options only). |
| `segment` | `string` | Exchange segment (e.g. `NFO-OPT`). |
