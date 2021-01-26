from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import AccountIn, AccountOut, AccountUpdate
from app.api import db_manager

accounts = APIRouter()

@accounts.get('/accounts', response_model=List[AccountOut])
async def getAllAccounts():
    return await db_manager.getAllAccounts()

@accounts.get('/accounts/{id}', response_model=AccountOut)
async def getAccountById(id: int):
    account = await db_manager.getAccountById(id)
    if not account:
        raise HTTPException(status_code=404, detail="Account with given id not found!")
    return account

@accounts.post('/accounts', response_model=AccountOut, status_code=201)
async def createAccount(request: AccountIn):
    account = await db_manager.getAccountById(request.id)
    if account:
        raise HTTPException(status_code=409, detail="Account with given id already exists!")
    account_id = await db_manager.createAccount(request)
    response = {
        'id': account_id,
        **request.dict()
    }
    return response

@accounts.put('/accounts/{id}', response_model=AccountOut)
async def updateAccount(id: int, request: AccountIn):
    account = await db_manager.getAccountById(id)
    if not account:
        raise HTTPException(status_code=404, detail="Account with given id not found!")
    update_data = request.dict(exclude_unset=True)
    account_in_db = AccountIn(**account)
    updated_account = account_in_db.copy(update=update_data)
    return await db_manager.updateAccount(id, updated_account)

@accounts.delete('/accounts/{id}', response_model=None)
async def deleteAccount(id: int):
    account = await db_manager.getAccountById(id)
    if not account:
        raise HTTPException(status_code=404, detail="Account with given id not found!")
    return await db_manager.deleteAccount(id)