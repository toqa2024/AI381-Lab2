
# AI381 Lab 2 — Customer Churn Prediction

[![CI](https://github.com/toqa2024/AI381-Lab2/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/toqa2024/AI381-Lab2/actions/workflows/ci.yml)

## Overview

This project trains a machine learning model to predict customer churn and serves predictions through a FastAPI application.

## Features

- Machine learning model training using scikit-learn.
- REST API built with FastAPI.
- Input validation using Pydantic.
- Automated tests using pytest.
- Multi-stage Docker build with a non-root user and health check.
- CI pipeline using GitHub Actions and Ruff.
- Docker security scanning using Trivy.
- Docker image publishing to GitHub Container Registry (GHCR).

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

Build and start the application:

```bash
docker build -t churn-api . && docker run --rm -p 8000:8000 churn-api
```

API endpoints:

- Health: `GET http://localhost:8000/health`
- Prediction: `POST http://localhost:8000/predict`
- Interactive documentation: `http://localhost:8000/docs`

## CI

GitHub Actions runs Ruff lint checks and pytest tests on pull requests and pushes to `main`.

The pipeline also builds the Docker image and scans it for HIGH and CRITICAL vulnerabilities using Trivy.

## Security and Deployment

The application runs in a multi-stage Docker image as a non-root user and includes a Docker health check.

After successful checks on `main`, GitHub Actions publishes the Docker image to GHCR using the commit SHA as its tag.

Container registry: `ghcr.io/toqa2024/ai381-lab2`

The `main` branch is protected by a ruleset requiring pull requests and successful status checks.
