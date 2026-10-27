# AI381 Lab 2 — MLOps Churn Prediction API

![CI](https://github.com/toqa2024/AI381-Lab2/actions/workflows/ci.yml/badge.svg)

## Overview
This project trains a machine learning model to predict customer churn and serves predictions through a FastAPI application.

## Features
- Machine learning model training using scikit-learn.
- REST API built with FastAPI.
- Input validation using Pydantic.
- Automated tests using pytest.
- Dockerized application with a health check.
- Continuous Integration using GitHub Actions and Ruff.

## Project Structure
```text
src/
  app/main.py
  train/train.py
tests/
models/
Dockerfile
requirements.txt
README.md
```

## Run Locally
Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn src.app.main:app --host 0.0.0.0 --port 8000
```

Open the API documentation at `http://localhost:8000/docs`.

## Run Tests

```bash
python -m pytest tests -v
```

## Run with Docker

```bash
docker build -t churn-api .
docker run --rm -p 8000:8000 churn-api
```

Health endpoint: `http://localhost:8000/health`

Prediction endpoint: `POST http://localhost:8000/predict`

## CI
GitHub Actions runs Ruff lint checks and pytest tests on pushes to `main` and pull requests targeting `main`.

## Security and Deployment
Security scanning with Trivy and publishing the Docker image to GitHub Container Registry (GHCR) are planned as part of the lab workflow.
