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

| Trigger | Target | Deploys | Runs the job |
|---|---|---|---|
| Pull request | dev | no | no |
| Push to `main` | **dev** | yes | no |
| Push tag `v*` | **prod** | yes | no |
| Actions tab -> Run workflow | your choice | yes | only if you tick `run_job` |

Deploying proves the job is installed correctly. Running it costs compute and
touches data, so it is opt-in rather than automatic on every push.

To release to prod:

    git tag v1.0.0 && git push origin v1.0.0

## Required GitHub secrets

Add these repository secrets before running the workflow:

- `DATABRICKS_HOST`
- `DATABRICKS_CLIENT_ID`
- `DATABRICKS_CLIENT_SECRET`

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
