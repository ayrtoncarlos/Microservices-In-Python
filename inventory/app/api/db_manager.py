from app.api.models import InventoryIn, InventoryOut, InventoryUpdate
from app.api.db import inventories, database

async def createInventory(request: InventoryIn):
    query = inventories.insert().values(**request.dict())
    return await database.execute(query=query)

async def getAllInventories():
    query = inventories.select()
    return await database.fetch_all(query=query)

async def getInventoryById(id):
    query = inventories.select(inventories.c.id==id)
    return await database.fetch_one(query=query)

async def deleteInventory(id: int):
    query = inventories.delete().where(inventories.c.id==id)
    return await database.execute(query=query)

async def updateInventory(id: int, request: InventoryIn):
    query = (inventories.update().where(inventories.c.id==id).values(**request.dict()))
    return await database.execute(query=query)
