from feast import FeatureStore


store = FeatureStore(repo_path=".")


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


entity_rows = [
    {"sample_id": 1}
]


result = store.get_online_features(
    features=features,
    entity_rows=entity_rows,
).to_dict()


print("Online features for sample_id=1:")
for key, value in result.items():
    print(f"{key}: {value}")