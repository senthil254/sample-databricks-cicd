# Databricks CI/CD Demo

This project is a simple end-to-end CI/CD example for Databricks.

### What it includes

- A Declarative Automation Bundles configuration in `databricks.yml`
- A demo Lakeflow Job definition in `resources/job.yml`
- A small Python module in `src/calculator.py`
- Unit tests in `tests/test_calculator.py`
- A demo notebook in `notebooks/demo_notebook.py`
- A GitHub Actions pipeline in `.github/workflows/ci-cd.yml`

## How the flow works

1. A developer pushes code to GitHub.
2. GitHub Actions installs Python dependencies.
3. Pytest runs the unit tests.
4. Databricks CLI validates the bundle.
5. On a push to `main`, the bundle is deployed to Databricks.
6. The deployed job runs the demo notebook for validation.

## Required GitHub secrets

Add these repository secrets before running the workflow:

- `DATABRICKS_HOST`
- `DATABRICKS_TOKEN`

## Local validation steps

From the project root, run:

- `pip install -r requirements.txt`
- `PYTEST_ADDOPTS='' PYTHONDONTWRITEBYTECODE=1 pytest -c pytest-ci.ini tests`
- `databricks bundle validate --target dev`

## Expected outcome

- Tests pass.
- Bundle validation succeeds.
- The bundle deploys to the Databricks workspace.
- The demo job completes successfully.

<!-- ci retrigger -->
