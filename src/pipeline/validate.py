import pandas as pd
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


class DataValidationError(Exception):
    pass


def validate(df):
    expected_columns = {
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
        "species",
        "sepal_area",
        "petal_area",
        "sepal_to_petal_length_ratio",
        "petal_length_bin",
    }

    if set(df.columns) != expected_columns:
        raise DataValidationError(
            f"Unexpected columns: {set(df.columns)}"
        )

    if df.isnull().any().any():
        raise DataValidationError("Null values detected")

    valid_species = {"setosa", "versicolor", "virginica"}

    if not set(df["species"]).issubset(valid_species):
        raise DataValidationError("Invalid species values")

    if not df["sepal length (cm)"].between(4.0, 8.0).all():
        raise DataValidationError("Invalid sepal length range")

    if not df["sepal width (cm)"].between(1.5, 5.0).all():
        raise DataValidationError("Invalid sepal width range")

    if not df["petal length (cm)"].between(1.0, 7.0).all():
        raise DataValidationError("Invalid petal length range")

    if not df["petal width (cm)"].between(0.1, 3.0).all():
        raise DataValidationError("Invalid petal width range")


if __name__ == "__main__":
    try:
        path = "data/processed/iris_features.csv"
        df = pd.read_csv(path)

        validate(df)

        logging.info(
            f"Validation passed: {len(df)} rows, {len(df.columns)} columns"
        )

    except DataValidationError as e:
        logging.error(f"Validation failed: {e}")
        sys.exit(1)