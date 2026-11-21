from racerapi.core.config import Settings


def test_settings_accept_environment_and_database_aliases():
    settings = Settings(
        APP_ENV="prod",
        SQL_DATABASE_URL="postgresql+psycopg://user:pass@localhost/app",
        LOG_LEVEL="DEBUG",
    )

    assert settings.app_env == "prod"
    assert settings.env == "prod"
    assert settings.database_url.startswith("postgresql")
    assert settings.log_level == "DEBUG"


def test_settings_support_legacy_environment_variable_names():
    settings = Settings(
        RACERAPI_ENV="test",
        RACERAPI_DATABASE_URL="sqlite+pysqlite:///:memory:",
        RACERAPI_LOG_LEVEL="INFO",
    )

    assert settings.env == "test"
    assert settings.database_url == "sqlite+pysqlite:///:memory:"


def test_default_settings_are_development_safe():
    settings = Settings()

    assert settings.env == "dev"
    assert settings.database_url.startswith("sqlite")
    assert settings.log_level == "INFO"
