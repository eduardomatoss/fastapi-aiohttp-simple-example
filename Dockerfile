FROM python:3.8.9-slim AS base

WORKDIR /app

COPY Pipfile .
RUN pip install pipenv

FROM base AS dependencies
RUN pipenv install --system --skip-lock

FROM base AS development
RUN pipenv install --system --dev --skip-lock
COPY . .

FROM dependencies AS production
COPY app app
COPY run.py .
COPY settings.toml .
