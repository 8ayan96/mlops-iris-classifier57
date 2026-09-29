import os
import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri(
    os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")
)

client = MlflowClient()

EXPERIMENT_NAME = "iris-classification-baseline"
REGISTERED_MODEL_NAME = "iris-classifier-prod"

experiment = client.get_experiment_by_name(EXPERIMENT_NAME)

if experiment is None:
    raise RuntimeError(f"Experiment not found: {EXPERIMENT_NAME}")

runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["metrics.f1_macro DESC"],
)

if not runs:
    raise RuntimeError("No runs found in the experiment.")

best_run = runs[0]
best_run_id = best_run.info.run_id

print("Best run:")
print("Run ID:", best_run_id)
print("Model:", best_run.data.params.get("model_type"))
print("F1:", best_run.data.metrics.get("f1_macro"))

model_uri = f"runs:/{best_run_id}/model"

print("\nRegistering model...")
result = mlflow.register_model(
    model_uri=model_uri,
    name=REGISTERED_MODEL_NAME,
)

print("Registered model:")
print("Name:", result.name)
print("Version:", result.version)

client.transition_model_version_stage(
    name=REGISTERED_MODEL_NAME,
    version=result.version,
    stage="Staging",
)

print("\nModel transitioned to Staging.")
print(f"Model URI: models:/{REGISTERED_MODEL_NAME}/Staging")