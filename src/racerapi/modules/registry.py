"""Compatibility registry for api.py-based module routers."""

from __future__ import annotations

from fastapi import APIRouter

_routers: list[APIRouter] = []


def register_router(router: APIRouter) -> None:
    """Register a router for inclusion during application bootstrap."""
    if router not in _routers:
        _routers.append(router)


def get_routers() -> list[APIRouter]:
    """Return registered routers without duplicates."""
    return list(_routers)


def clear_routers() -> None:
    """Clear the compatibility registry (primarily useful in tests)."""
    _routers.clear()
