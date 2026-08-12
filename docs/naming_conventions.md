# Contract Naming Conventions

This document explains the standard contract trading symbol formatting used in OptionVault. OptionVault strictly matches the National Stock Exchange (NSE) format for standard trading terminals.

## 1. Futures Contract Naming

Futures symbols follow a fixed format:

```
[UNDERLYING][YY][MMM]FUT
```

- **`UNDERLYING`**: The asset name (e.g. `NIFTY`, `BANKNIFTY`, `RELIANCE`).
- **`YY`**: 2-digit expiry year (e.g. `25` for 2025).
- **`MMM`**: 3-letter month abbreviation (`JAN`, `FEB`, `MAR`, `APR`, `MAY`, `JUN`, `JUL`, `AUG`, `SEP`, `OCT`, `NOV`, `DEC`).
- **`FUT`**: Futures suffix.

### Examples:
*   `NIFTY25JANFUT` — NIFTY Index Futures expiring in January 2025.
*   `RELIANCE26JULFUT` — RELIANCE Stock Futures expiring in July 2026.

---

## 2. Options Contract Naming

Options contracts differ depending on whether they are **weekly** or **monthly** expiries.

### Monthly Options Format
Monthly options expire on the last Thursday of the month:

```
[UNDERLYING][YY][MMM][STRIKE][SIDE]
```

- **`SIDE`**: `CE` for Call, `PE` for Put.
- **`STRIKE`**: Strike price value (e.g. `14000`, `2500`).

#### Examples:
*   `NIFTY25JAN24000CE` — NIFTY January 2025 Strike 24000 Call.
*   `RELIANCE26JUL1300PE` — RELIANCE July 2026 Strike 1300 Put.

### Weekly Options Format
Weekly options expire every Thursday (except the monthly expiry week):

```
[UNDERLYING][YY][M][DD][STRIKE][SIDE]
```

- **`M`**: 1-digit code for Month:
  - `1` = Jan, `2` = Feb, ..., `9` = Sep, `O` = Oct, `N` = Nov, `D` = Dec.
- **`DD`**: 2-digit expiry day (e.g. `18` for 18th).

#### Examples:
*   `NIFTY2511824200CE` — NIFTY expiring on **January 18, 2025**, Strike 24200 Call (Weekly).
*   `BANKNIFTY26D0552500PE` — BANKNIFTY expiring on **December 5, 2026**, Strike 52500 Put (Weekly).
