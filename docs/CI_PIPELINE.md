# CI Pipeline Documentation

## 1. Overview

This document describes the Continuous Integration (CI) pipeline implemented
using GitHub Actions for the Iris Classifier project.

The pipeline automatically checks code quality, runs the test suite, and
verifies model quality before changes are merged into the main branch.

## 2. CI Pipeline Jobs

The CI pipeline consists of three jobs:

### 2.1 Build and Lint

- Checks the Python source code for linting issues.
- Uses Flake8 to identify coding errors and style violations.
- Ensures that the code follows the defined quality standards.

### 2.2 Test Suite

- Runs the project's automated tests.
- Verifies that the application and its components work as expected.
- Runs only after the Build and Lint job succeeds.

### 2.3 Model Quality Gate

- Evaluates the trained model's accuracy.
- Checks whether the model meets the minimum acceptable accuracy.
- Runs only after the Test Suite job succeeds.

## 3. Job Dependencies

The jobs execute in the following order:

1. Build and Lint
2. Test Suite
3. Model Quality Gate

The Test Suite depends on Build and Lint, while Model Quality Gate
depends on the Test Suite.

If an earlier job fails, dependent jobs are not executed.

## 4. Branch Protection Rules

Branch protection rules are configured for the `main` branch.

The configured rules include:

- Pull requests are required before merging.
- Required CI status checks must pass.
- Force pushes are blocked.
- Branch deletion is restricted.

The required status checks are:

- `build-and-lint`
- `test-suite`
- `model-quality-gate`

## 5. Successful CI Pipeline Verification

A pull request was created to verify the CI pipeline.

**Pull Request #4:** Experiment 9: Continuous Integration Pipeline Setup Using GitHub Actions

All three CI jobs completed successfully:

- Build and Lint — Passed
- Test Suite — Passed
- Model Quality Gate — Passed

The pull request was successfully merged into the `main` branch.

## 6. Model Quality Regression Demonstration

A temporary branch named `feature/simulate-regression` was created
to demonstrate the model quality gate.

The minimum acceptable accuracy threshold was temporarily increased
from `0.90` to `0.999` in the model quality test.

A pull request was created to trigger the CI pipeline.

**Observed CI results:**

- Build and Lint — Passed
- Test Suite — Failed
- Model Quality Gate — Skipped

This demonstrated that the CI pipeline correctly detects a model
quality regression and prevents dependent jobs from running.

The regression demonstration pull request was closed without merging.

The original threshold of `0.90` was verified on the `main` branch,
and the temporary local branch was deleted.

## 7. Conclusion

The GitHub Actions CI pipeline automates code linting, test execution,
and model quality verification.

Branch protection rules help ensure that changes are reviewed and
required CI checks pass before merging into the `main` branch.