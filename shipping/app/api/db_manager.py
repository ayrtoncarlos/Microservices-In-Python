from app.api.models import ShippingIn, ShippingOut, ShippingUpdate
from app.api.db import shipments, database

async def createShipping(request: ShippingIn):
    query = shipments.insert().values(**request.dict())
    return await database.execute(query=query)

async def getAllShipments():
    query = shipments.select()
    return await database.fetch_all(query=query)

async def getShippingById(id):
    query = shipments.select(shipments.c.id==id)
    return await database.fetch_one(query=query)

async def deleteShipping(id: int):
    query = shipments.delete().where(shipments.c.id==id)
    return await database.execute(query=query)

async def updateShipping(id: int, request: ShippingIn):
    query = (shipments.update().where(shipments.c.id==id).values(**request.dict()))
    return await database.execute(query=query)
