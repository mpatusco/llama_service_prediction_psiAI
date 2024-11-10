from pymongo import MongoClient
from app.config.settings import DATABASE_URL

client = MongoClient(DATABASE_URL)
db = client["persona_info"]

async def fetch_persona_by_key(key: str):
    """Fetch persona data from MongoDB based on a unique key.

    Args:
        key (str): Unique identifier for the persona document.

    Returns:
        dict: The persona document matching the key.
    """
    return db.personas.find_one({"_id": key})
