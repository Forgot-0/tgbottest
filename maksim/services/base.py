from motor.core import AgnosticCollection
from domain.user import User
from domain.utils import PyObjectId

class BaseService:
    def __init__(self, collection: AgnosticCollection) -> None:
        self.collection = collection
    
    async def save(self, data: dict):
        res = await self.collection.insert_one(data)
        return res
    
    async def delete(self, id: PyObjectId):
        res = await self.collection.delete_one({'_id': id})
        return res
    
    async def update(self, id: PyObjectId, data: dict):
        res = await self.collection.update_one({'_id': id}, update=data)
        return res