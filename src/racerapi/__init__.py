"""RacerAPI: a modular, NestJS-inspired Python framework."""

__version__ = "1.0.0"

from racerapi.core.bootstrap import create_app

__all__ = ["__version__", "create_app"]
