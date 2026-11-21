# Module System

A feature module represents one cohesive business capability. Keep module-specific routes, schemas, services, repositories, models, and tests together.

```text
modules/<feature>/
├── __init__.py
├── api.py
├── service.py
├── repo.py
├── models.py
├── schemas.py
├── deps.py
└── tests/
```

## Registration contract

For modules requiring explicit bootstrap, expose a `register(container, app)` function in `module.py`. RacerAPI discovers the module entrypoint and passes the application-scoped dependency container and FastAPI application.

Legacy modules can expose `api.py` and register an `APIRouter` using `racerapi.modules.registry.register_router`. New modules should prefer explicit module registration.

## Boundaries

Modules should not import private implementation files from other modules. Share cross-cutting contracts through explicit provider interfaces or a dedicated shared package.
