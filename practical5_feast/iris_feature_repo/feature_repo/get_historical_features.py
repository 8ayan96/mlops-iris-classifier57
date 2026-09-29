import pandas as pd
from feast import FeatureStore

store = FeatureStore(repo_path=".")

entity_df = pd.read_parquet(
    "data/iris_features.parquet"
)[["sample_id", "event_timestamp"]].head(5)

features = [
    "iris_measurements:sepal length (cm)",
    "iris_measurements:sepal width (cm)",
    "iris_measurements:petal length (cm)",
    "iris_measurements:petal width (cm)",
    "iris_engineered_features:sepal_area",
    "iris_engineered_features:petal_area",
    "iris_engineered_features:sepal_to_petal_length_ratio",
    "iris_engineered_features:petal_length_bin",
]

training_df = store.get_historical_features(
    entity_df=entity_df,
    features=features,
).to_df()

print("Historical features:")
print(training_df)
print(f"\nRows returned: {len(training_df)}")