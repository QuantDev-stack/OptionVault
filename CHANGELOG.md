# Changelog

All notable changes to the OptionVault dataset schema, coverage, and API tooling will be documented in this file.

## [1.0.0] - 2026-07-19

### Added
- Initial public release of OptionVault sample datasets.
- Cash (SPOT) market data samples for `ACC`, `RELIANCE`, `TCS`, and `NIFTY50`.
- Futures market data samples for `NIFTY`, `BANKNIFTY`, and `RELIANCE` indices/stocks.
- Options market data samples featuring strike-level Call/Put details.
- Real-time Greeks calculation pipeline logs (including Delta, Gamma, Theta, Vega, IV, Vanna, Charm, Vomma, Speed, Zomma, and Color).
- 1-Second OHLCV resampled index bars and raw tick-level datasets for `NIFTY50`.
- Level 2 Order Book snapshot samples demonstrating depth levels 1 to 5.
- Multi-commodity Exchange (MCX) Futures and Options datasets for `COPPER`.
- Documentation pages covering naming conventions, schemas, dictionaries, and dataset coverage.
- Code examples for querying and processing datasets using Python, Pandas, and Polars.
