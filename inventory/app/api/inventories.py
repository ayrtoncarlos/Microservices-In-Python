from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import InventoryIn, InventoryOut, InventoryUpdate
from app.api import db_manager

inventories = APIRouter()

@inventories.get('/inventories', response_model=List[InventoryOut])
async def getAllInventories():
    return await db_manager.getAllInventories()

@inventories.get('/inventories/{id}', response_model=InventoryOut)
async def getInventoryById(id: int):
    inventory = await db_manager.getInventoryById(id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory with given id not found!")
    return inventory

@inventories.post('/inventories', response_model=InventoryOut, status_code=201)
async def createInventory(request: InventoryIn):
    inventory = await db_manager.getInventoryById(request.id)
    if inventory:
        raise HTTPException(status_code=409, detail="Inventory with given id already exists!")
    inventory_id = await db_manager.createInventory(request)
    response = {
        'id': inventory_id,
        **request.dict()
    }
    return response

@inventories.put('/inventories/{id}', response_model=InventoryOut)
async def updateInventory(id: int, request: InventoryIn):
    inventory = await db_manager.getInventoryById(id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory with given id not found!")
    update_data = request.dict(exclude_unset=True)
    inventory_in_db = InventoryIn(**inventory)
    updated_inventory = inventory_in_db.copy(update=update_data)
    return await db_manager.updateInventory(id, updated_inventory)

@inventories.delete('/inventories/{id}', response_model=None)
async def deleteInventory(id: int):
    inventory = await db_manager.getInventoryById(id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory with given id not found!")
    return await db_manager.deleteInventory(id)