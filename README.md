<p align="center">
  <img src="assets/racerapi-logo.png" alt="RacerAPI Logo"/>
</p>

<h1 align="center">RacerAPI</h1>
<p align="center">A modular, NestJS-inspired Python framework powered by FastAPI.</p>

---

## What is RacerAPI?

RacerAPI provides a structured application framework for building modular Python APIs. It combines FastAPI's ASGI foundation with a NestJS-style developer experience: modules, controllers/routes, services, repositories, dependency injection, plugins, CLI generators, and explicit application bootstrap.

**Architecture:** `Module → Controller/API → Service → Repository → Database`

## Requirements

- Python 3.11+
- Poetry 1.8+
- Optional: a supported SQL database or MongoDB integration

## Create an application

```bash
poetry new my-api
cd my-api
poetry add racerapi
poetry add fastapi uvicorn
```

Or generate a project using the framework CLI:

```bash
racerapi new my-api --db sql
cd my-api
poetry install
poetry run racerapi dev
```

## Generate a feature module

```bash
racerapi generate module products
```

Generated modules follow a predictable structure:

```text
modules/products/
├── api.py
├── service.py
├── repo.py
├── models.py
├── schemas.py
├── deps.py
└── tests/
```

## Application bootstrap

```python
from racerapi import create_app

app = create_app(title="Store API")
```

Run with:

```bash
uvicorn main:app --reload
```

## Core capabilities

- Modular application structure and module discovery
- FastAPI-native request validation and dependency overrides
- Application-scoped dependency injection container
- Plugin registration hooks
- SQLAlchemy database layer and Alembic migration commands
- CLI for project/module generation, database operations, diagnostics and runtime
- Request-aware structured logging
- Architecture rules and test support

## Development

```bash
poetry install --with dev
poetry run pytest -q
poetry run ruff check src tests
poetry build
```

## Compatibility and stability

RacerAPI 1.0.0 establishes the supported public baseline: `racerapi.create_app`, the `racerapi` CLI entrypoint, Poetry project management, and the documented module contract. Internal modules are not guaranteed as public extension points unless documented.

## Documentation

See the [RacerAPI documentation](https://strix-engineering-studio.github.io/racerapi/).

## License

MIT. See [LICENSE.md](LICENSE.md).
