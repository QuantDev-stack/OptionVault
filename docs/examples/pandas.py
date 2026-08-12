import pandas as pd
import numpy as np

def load_and_clean_data(file_path):
    print(f"Loading dataset from: {file_path}...")
    df = pd.read_csv(file_path)
    
    # Convert datetime column
    if "datetime" in df.columns:
        df["datetime"] = pd.to_datetime(df["datetime"])
    elif "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df.rename(columns={"timestamp": "datetime"}, inplace=True)
        
    print(f"Loaded {len(df)} rows. Columns: {df.columns.tolist()}")
    return df

def calculate_vwap(df):
    """Calculate Volume Weighted Average Price (VWAP)."""
    print("\nCalculating VWAP...")
    df["typical_price"] = (df["high"] + df["low"] + df["close"]) / 3
    df["price_volume"] = df["typical_price"] * df["volume"]
    
    # Cumulative calculations
    df["cum_price_volume"] = df["price_volume"].cumsum()
    df["cum_volume"] = df["volume"].cumsum()
    
    df["vwap"] = df["cum_price_volume"] / df["cum_volume"]
    print(df[["datetime", "close", "volume", "vwap"]].head())
    return df

def resample_ohlc(df, interval="5min"):
    """Resample 1-minute data into higher intervals (e.g. 5-minute OHLCV)."""
    print(f"\nResampling data to {interval} OHLCV bars...")
    df.set_index("datetime", inplace=True)
    
    resampled = df.resample(interval).agg({
        "open": "first",
        "high": "max",
        "low": "min",
        "close": "last",
        "volume": "sum",
        "oi": "last"
    }).dropna()
    
    resampled.reset_index(inplace=True)
    print(resampled.head())
    return resampled

if __name__ == "__main__":
    # Test with sample cash data
    sample_file = "../../samples/cash/RELIANCE.csv"
    try:
        df = load_and_clean_data(sample_file)
        df_vwap = calculate_vwap(df)
        df_5m = resample_ohlc(df_vwap)
    except FileNotFoundError:
        # If running from different CWD, fallback to absolute path check
        print("Sample file not found. Run from the examples directory.")
