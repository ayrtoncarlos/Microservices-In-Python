from app.api.models import OrderIn, OrderOut, OrderUpdate
from app.api.db import orders, database

async def createOrder(request: OrderIn):
    query = orders.insert().values(**request.dict())
    return await database.execute(query=query)

async def getAllOrders():
    query = orders.select()
    return await database.fetch_all(query=query)

async def getOrderById(id):
    query = orders.select(orders.c.id==id)
    return await database.fetch_one(query=query)

async def deleteOrder(id: int):
    query = orders.delete().where(orders.c.id==id)
    return await database.execute(query=query)

async def updateOrder(id: int, request: OrderIn):
    query = (orders.update().where(orders.c.id==id).values(**request.dict()))
    return await database.execute(query=query)
