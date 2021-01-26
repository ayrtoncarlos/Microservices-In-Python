from app.api.models import AccountIn, AccountOut, AccountUpdate
from app.api.db import accounts, database

async def createAccount(request: AccountIn):
    query = accounts.insert().values(**request.dict())
    return await database.execute(query=query)

async def getAllAccounts():
    query = accounts.select()
    return await database.fetch_all(query=query)

async def getAccountById(id):
    query = accounts.select(accounts.c.id==id)
    return await database.fetch_one(query=query)

async def deleteAccount(id: int):
    query = accounts.delete().where(accounts.c.id==id)
    return await database.execute(query=query)

async def updateAccount(id: int, request: AccountIn):
    query = (accounts.update().where(accounts.c.id==id).values(**request.dict()))
    return await database.execute(query=query)
