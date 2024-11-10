import os
from dotenv import load_dotenv

load_dotenv()

"""Settings configuration for the application.

This module loads environment variables for configuration, such as the
MongoDB connection URL.

Attributes:
    DATABASE_URL (str): The MongoDB connection string.
"""


DATABASE_URL = os.getenv("DATABASE_URL", "mongodb://localhost:27017/")
