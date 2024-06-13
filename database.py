from motor.core import AgnosticClient, AgnosticDatabase
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DATABASE = "fastapicrud"


class MongoConnection:
    _connection = None

    @classmethod
    async def get_connection(cls) -> AgnosticClient:
        """Return Mongo connection from creds.

        Returns
        -------
        AgnosticClient
        """
        MONGO_URI = "mongodb://root:secret@mongo:27017/"
        if cls._connection is None:
            cls._connection = AsyncIOMotorClient(MONGO_URI)
        return cls._connection

    @classmethod
    async def close_connection(cls):
        if cls._connection:
            cls._connection.close()
            cls._connection = None


async def get_db() -> AgnosticDatabase:
    """Return Mongo connection with db selected.

    Returns
    -------
    AgnosticDatabase
    """
    client = await MongoConnection.get_connection()
    db = client[MONGO_DATABASE]  # Replace with your database name
    await create_index(db)
    return db


async def create_index(db: AgnosticDatabase):
    """Create index on db.

    Parameters
    ----------
    db : AgnosticDatabase
    """
    await db.items.create_index("name", unique=True)
