# Data Pipeline Documentation

## Overview

This project implements an automated data pipeline for the Iris dataset using Python and DVC.

The pipeline consists of four stages:

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Data Validation

The stages are connected using DVC to provide reproducibility and pipeline automation.

## Pipeline Flow

Collect
   ↓
Preprocess
   ↓
Features
   ↓
Validate

## 1. Data Collection

File: `src/pipeline/collect.py`

The data collection stage uses the Iris dataset and creates the raw dataset.

Output:

`data/raw/iris_raw.csv`

The collected dataset contains 150 rows.

## 2. Data Preprocessing

File: `src/pipeline/preprocess.py`

The preprocessing stage:

- Removes duplicate rows
- Converts numeric columns to numeric data types
- Fills missing numeric values using the median
- Removes rows with missing species values
- Removes the `collected_at` column

Output:

`data/processed/iris_preprocessed.csv`

After preprocessing, the dataset contains 149 rows.

## 3. Feature Engineering

File: `src/pipeline/features.py`

The feature engineering stage creates additional features:

- `sepal_area`
- `petal_area`
- `sepal_to_petal_length_ratio`
- `petal_length_bin`

Output:

`data/processed/iris_features.csv`

The final feature dataset contains 9 columns.

## 4. Data Validation

File: `src/pipeline/validate.py`

The validation stage checks:

- Expected columns are present
- No null values exist
- Species values are valid
- Numeric values are within expected ranges

The validation completed successfully with:

- 149 rows
- 9 columns

## DVC Pipeline

The pipeline is defined in `dvc.yaml`.

DVC manages the dependencies, outputs, and execution order of each stage.

The pipeline can be executed using:

dvc repro

If no files or dependencies have changed, DVC skips the stages and reports that the data and pipeline are up to date.

## DVC Remote

A DVC remote named `myremote` is configured for storing DVC-tracked data and artifacts.

The data was successfully pushed using:

dvc push

## Verification

The pipeline was verified using:

dvc repro
dvc dag
dvc push

The pipeline executed successfully and the DVC data was pushed to the configured remote storage.

## Conclusion

The automated data pipeline successfully performs data collection, preprocessing, feature engineering, and validation. DVC provides pipeline automation, reproducibility, caching, and data versioning for the project.