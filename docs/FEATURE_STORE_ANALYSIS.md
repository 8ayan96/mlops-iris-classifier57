# Feature Store Analysis

## Overview

Feast was implemented as a centralized Feature Store for the Iris dataset. It provides a single place to define, register, materialize, retrieve, and reuse features across different model workflows.

## Observed Benefits

### 1. Elimination of Training-Serving Skew

The same `iris_engineered_features` definitions are used for both online and offline feature retrieval.

- Online features were retrieved using Feast in Step 6.
- Historical/offline features were retrieved using Feast in Step 7.
- The same registered feature definitions are used in both workflows.

This helps maintain consistency between features used during model training and features served for inference.

### 2. Feature Reusability

The registered features can be reused by another model without re-implementing the feature engineering logic.

In Step 8, the `iris_feature_service` was used to retrieve the registered Iris features through Feast.

The Feature Service provided:

- Sepal length
- Sepal width
- Petal length
- Petal width
- Sepal area
- Petal area
- Sepal-to-petal length ratio
- Petal length bin

This demonstrates that the same centrally registered features can be consumed by a different model workflow.

### 3. Centralized Governance

The `features.py` file acts as the central source of truth for the registered entities, Feature Views, and Feature Service.

The Feature Store provides centralized management of:

- Entity definition
- Feature definitions
- Feature Views
- Feature Service
- Online feature storage
- Offline/historical feature retrieval

This improves consistency and makes feature definitions easier to manage and reuse across consuming models.

## Conclusion

The Feast Feature Store successfully provides centralized feature management, consistent online and offline retrieval, and reusable registered features for different model workflows.

The Experiment 5 implementation demonstrates how a Feature Store can support feature definition, registration, materialization, retrieval, and reuse within an MLOps workflow.