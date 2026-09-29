import pandas as pd
from pathlib import Path


# Experiment 4 feature output
input_path = Path(
    r"C:/Users/ASUS/mlops-iris-classifier/mlops-iris-classifier57/data/processed/iris_features.csv"
)

# Feast feature source output
output_path = Path("data/iris_features.parquet")

# Load Experiment 4 features
df = pd.read_csv(input_path)

# Add Feast entity key
df["sample_id"] = range(len(df))

# Add event timestamps
df["event_timestamp"] = pd.date_range(
    start="2026-08-15 15:20:02",
    periods=len(df),
    freq="min",
    tz="UTC",
)

# Created timestamp
df["created_timestamp"] = df["event_timestamp"]

# Save as Parquet
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_parquet(output_path, index=False)

print(f"Saved {len(df)} rows to {output_path}")
print(f"Columns: {len(df.columns)}")
print(df.head())