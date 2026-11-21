# Getting Started

## Requirements

- Python 3.11 or newer
- Poetry 1.8 or newer

## Install

Create a project and add RacerAPI:

```bash
poetry new inventory-api
cd inventory-api
poetry add racerapi
poetry add uvicorn
```

## Bootstrap an application

Create `main.py`:

```python
from racerapi import create_app

app = create_app(title="Inventory API")
```

Run it:

```bash
poetry run uvicorn main:app --reload
```

## Generate a project

The CLI can scaffold a project with Poetry metadata:

```bash
racerapi new inventory_api --db sql
cd inventory_api
poetry install
poetry run racerapi dev
```

## Generate a module

```bash
racerapi generate module products
```

A generated module contains API routes, a service, repository, database models, Pydantic schemas, dependency providers, and tests.

## Environment

RacerAPI reads configuration from environment variables and an optional `.env` file.

```env
APP_ENV=dev
SQL_DATABASE_URL=sqlite+pysqlite:///./app.db
MONGO_DATABASE_URL=mongodb://localhost:27017/app
LOG_LEVEL=INFO
```

Use Alembic migrations to evolve production database schemas. Do not create production tables automatically during application startup.
