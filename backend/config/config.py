import os
from functools import lru_cache

from logger import logger

if os.environ.get("ENVIRONMENT", "").upper() != "PRODUCTION":
    logger.info("Loading development environment variables")
    os.environ["JWT_SECRET"] = "secret"
    os.environ["JWT_ALGORITHM"] = "HS256"
    os.environ["JWT_EXPIRE_MINUTES"] = "30"
    os.environ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
else:
    logger.info("Loading production environment variables")


@lru_cache
def get_env_variable(var_name):
    """Get the environment variable or return exception."""
    try:
        logger.info(f"{var_name} loaded from environment")
        return os.environ[var_name]
    except KeyError:
        error_msg = f"Set the {var_name} environment variable"
        logger.error(error_msg)
        raise EnvironmentError(error_msg)


class Config:
    """Set Flask configuration vars from .env file."""

    ENVIRONMENT = get_env_variable("ENVIRONMENT")
    JWT_SECRET = get_env_variable("JWT_SECRET")
    JWT_ALGORITHM = get_env_variable("JWT_ALGORITHM")
    JWT_EXPIRE_MINUTES = float(get_env_variable("JWT_EXPIRE_MINUTES"))
    SQLALCHEMY_DATABASE_URI = get_env_variable("SQLALCHEMY_DATABASE_URI")
