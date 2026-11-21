"""Default ASGI entrypoint for applications generated with RacerAPI."""

from racerapi import create_app

app = create_app()


def run() -> None:
    """Run the default ASGI application."""
    import uvicorn

    uvicorn.run("racerapi.main:app", host="127.0.0.1", port=8000, reload=False)


if __name__ == "__main__":
    run()
