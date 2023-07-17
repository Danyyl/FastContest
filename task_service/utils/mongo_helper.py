from typing import List

from motor.motor_asyncio import AsyncIOMotorClient


class MongoHelper:
    def __init__(self):
        self.client = AsyncIOMotorClient("mongodb://contest:contest@localhost:27017")
        self.db = self.client.contest_db

    async def get_object(self, collection: str, params: dict):
        result = await self.db[collection].find_one(params)
        return result

    async def get_objects(self, collection: str, params: dict):
        result = [item async for item in self.db[collection].find(params)]
        return result

    async def insert_one(self, collection: str, data: dict):
        result = await self.db[collection].insert_one(data)
        return result.inserted_id

    async def insert_many(self, collection: str, data: List[dict]):
        result = await self.db[collection].insert_many(data)
        return result.inserted_ids
