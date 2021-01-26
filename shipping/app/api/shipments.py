from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import ShippingIn, ShippingOut, ShippingUpdate
from app.api import db_manager

shipments = APIRouter()

@shipments.get('/shipments', response_model=List[ShippingOut])
async def getAllShipments():
    return await db_manager.getAllShipments()

@shipments.get('/shipments/{id}', response_model=ShippingOut)
async def getShippingById(id: int):
    shipping = await db_manager.getShippingById(id)
    if not shipping:
        raise HTTPException(status_code=404, detail="Shipping with given id not found!")
    return shipping

@shipments.post('/shipments', response_model=ShippingOut, status_code=201)
async def createShipping(request: ShippingIn):
    shipping = await db_manager.getShippingById(request.id)
    if shipping:
        raise HTTPException(status_code=409, detail="Shipping with given id already exists!")
    shipping_id = await db_manager.createShipping(request)
    response = {
        'id': shipping_id,
        **request.dict()
    }
    return response

@shipments.put('/shipments/{id}', response_model=ShippingOut)
async def updateShipping(id: int, request: ShippingIn):
    shipping = await db_manager.getShippingById(id)
    if not shipping:
        raise HTTPException(status_code=404, detail="Shipping with given id not found!")
    update_data = request.dict(exclude_unset=True)
    shipping_in_db = ShippingIn(**shipping)
    updated_shipping = shipping_in_db.copy(update=update_data)
    return await db_manager.updateShipping(id, updated_shipping)

@shipments.delete('/shipments/{id}', response_model=None)
async def deleteShipping(id: int):
    shipping = await db_manager.getShippingById(id)
    if not shipping:
        raise HTTPException(status_code=404, detail="Shipping with given id not found!")
    return await db_manager.deleteShipping(id)