# Regime Radar

A web app that detects market regimes — calm bull markets, volatile selloffs, sideways chop — and shows how simple strategies perform in each one.

> 🚧 Work in progress. Live demo link coming soon.

## What it does

1. **Data** — daily prices for major ETFs (SPY, QQQ, TLT, GLD, sectors) plus macro series from FRED (VIX, yield curve, credit spreads).
2. **Features** — rolling volatility, trend, cross-asset correlation, yield-curve slope. Every feature uses only past data (no lookahead).
3. **Regimes** — unsupervised regime detection with a KMeans baseline and a Gaussian Hidden Markov Model, fit on past data and applied forward.
4. **Backtests** — buy-and-hold, 60/40, and regime-switching strategies, evaluated walk-forward with transaction costs.
5. **Dashboard** — an interactive Streamlit app with regime-shaded charts and strategy comparisons.

## Tech stack

Python · pandas · scikit-learn · hmmlearn · Plotly · Streamlit · pytest · GitHub Actions

## Run locally

_Setup instructions coming soon._

## License

[MIT](LICENSE)