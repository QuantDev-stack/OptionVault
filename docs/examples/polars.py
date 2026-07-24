import polars as pl

def load_and_clean_data(file_path):
    print(f"Loading dataset via Polars from: {file_path}...")
    
    df = pl.read_csv(file_path)
    if "datetime" in df.columns:
        df = df.with_columns(pl.col("datetime").str.to_datetime())
    elif "timestamp" in df.columns:
        df = df.with_columns(pl.col("timestamp").str.to_datetime())
        df = df.rename({"timestamp": "datetime"})
        
    print(f"Loaded {df.height} rows. Columns: {df.columns}")
    return df

def calculate_vwap(df):
    """Calculate Volume Weighted Average Price (VWAP) using Polars expressions."""
    print("\nCalculating VWAP with Polars expressions...")
    
    df = df.with_columns([
        ((pl.col("high") + pl.col("low") + pl.col("close")) / 3).alias("typical_price")
    ])
    
    df = df.with_columns([
        (pl.col("typical_price") * pl.col("volume")).alias("price_volume")
    ])
    
    df = df.with_columns([
        pl.col("price_volume").cum_sum().alias("cum_price_volume"),
        pl.col("volume").cum_sum().alias("cum_volume")
    ])
    
    df = df.with_columns([
        (pl.col("cum_price_volume") / pl.col("cum_volume")).alias("vwap")
    ])
    
    print(df.select(["datetime", "close", "volume", "vwap"]).head(5))
    return df

def resample_ohlc(df, interval="5m"):
    """Resample OHLCV bars using Polars group_by_dynamic."""
    print(f"\nResampling data to {interval} intervals...")
    
    # Sort is required for dynamic group_by
    df = df.sort("datetime")
    
    resampled = df.group_by_dynamic("datetime", every=interval).agg([
        pl.col("open").first().alias("open"),
        pl.col("high").max().alias("high"),
        pl.col("low").min().alias("low"),
        pl.col("close").last().alias("close"),
        pl.col("volume").sum().alias("volume"),
        pl.col("oi").last().alias("oi")
    ])
    
    print(resampled.head(5))
    return resampled

if __name__ == "__main__":
    sample_file = "../../samples/cash/RELIANCE.csv"
    try:
        df = load_and_clean_data(sample_file)
        df_vwap = calculate_vwap(df)
        df_5m = resample_ohlc(df_vwap)
    except Exception as e:
        print(f"Failed to run Polars example: {e}")
        print("Note: Ensure polars is installed (`pip install polars`) and the CSV exists.")
