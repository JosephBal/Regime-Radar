"""Project-wide settings for Regime Radar."""
from pathlib import Path

# Folders
ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"

# Market data (Yahoo Finance)
TICKERS = ["SPY", "QQQ", "IWM", "TLT", "GLD", "XLK", "XLF", "XLE"]

# Macro data (FRED series IDs)
FRED_SERIES = {
    "vix": "VIXCLS",             # Volatility index
    "yield_curve": "T10Y2Y",     # 10-year minus 2-year Treasury spread
    "credit_spread": "BAA10Y",  # High-yield bond spread
}

# Date range
START_DATE = "2005-01-01"

# Regime model train/test split
TRAIN_END = "2015-12-31"