import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base Config class"""

    SECRET_KEY = os.environ.get("SECRET_KEY", "defaulthardtoguessstring")


class DevelopmentConfig(Config):
    """Config class for development"""

    DEBUG = True


class TestConfig(Config):
    """Config class for testing"""

    TESTING = True


lookup = {"development": DevelopmentConfig, "test": TestConfig}

env = os.getenv("ENVIRONMENT", "development")
config = lookup[env]
