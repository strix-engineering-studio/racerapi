from __future__ import annotations

import importlib
import pkgutil
from pathlib import Path

from fastapi import FastAPI

from racerapi import __version__
from racerapi.core.config.settings import get_settings
from racerapi.core.di import Container
from racerapi.core.logger import configure_logging, get_logger
from racerapi.core.plugins.loader import load_plugins, register_app_plugins
from racerapi.modules import registry as modules_registry

logger = get_logger(__name__)


def create_app(
    title: str = "RacerAPI",
    version: str = __version__,
    *,
    discover_builtin_modules: bool = True,
) -> FastAPI:
    """Create a FastAPI app with an isolated DI container and configured modules."""
    settings = get_settings()
    configure_logging(settings.log_level)

    container = Container()
    container.register(type(settings), settings, scope="singleton")
    container.register("settings", settings, scope="singleton")
    container.register(Container, container, scope="singleton")

    plugins = load_plugins(settings, container=container)
    app = FastAPI(title=title, version=version)
    app.state.container = container
    register_app_plugins(app, plugins)

    if discover_builtin_modules:
        import racerapi.modules as modules_pkg

        for _, name, ispkg in pkgutil.iter_modules(modules_pkg.__path__):
            if not ispkg or name.startswith("_"):
                continue

            package_dir = Path(modules_pkg.__file__).parent / name
            module_entry = package_dir / "module.py"
            api_entry = package_dir / "api.py"

            if module_entry.is_file():
                module = importlib.import_module(f"racerapi.modules.{name}.module")
                register = getattr(module, "register", None)
                if callable(register):
                    register(container, app)
            elif api_entry.is_file():
                importlib.import_module(f"racerapi.modules.{name}.api")

    for router in modules_registry.get_routers():
        app.include_router(router)

    @app.get("/", tags=["system"], include_in_schema=False)
    def root() -> dict[str, str]:
        return {"status": "ok", "environment": settings.app_env}

    return app


__all__ = ["create_app"]
