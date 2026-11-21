# Dependency Injection

RacerAPI creates an application-scoped `Container` and attaches it to `app.state.container`. Providers can be registered as singleton or transient services.

```python
from racerapi.core.di import Container

container = Container()
container.register("mailer", Mailer, scope="singleton")
mailer = container.resolve("mailer")
```

Use FastAPI's native `Depends` for request-scoped dependencies. The `provide(token)` helper bridges a registered container provider into FastAPI dependency injection.

```python
from fastapi import APIRouter
from racerapi.core.di_fastapi import provide

router = APIRouter()

@router.get("/status")
def status(mailer = provide("mailer")):
    return {"ready": mailer is not None}
```

Prefer explicit provider registration for infrastructure services. Avoid hidden global containers; each app instance owns its container.
