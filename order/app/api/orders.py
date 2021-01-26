from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import OrderIn, OrderOut, OrderUpdate
from app.api import db_manager

orders = APIRouter()

@orders.get('/orders', response_model=List[OrderOut])
async def getAllOrders():
    return await db_manager.getAllOrders()

@orders.get('/orders/{id}', response_model=OrderOut)
async def getOrderById(id: int):
    order = await db_manager.getOrderById(id)
    if not order:
        raise HTTPException(status_code=404, detail="Order with given id not found!")
    return order

@orders.post('/orders', response_model=OrderOut, status_code=201)
async def createOrder(request: OrderIn):
    order = await db_manager.getOrderById(request.id)
    if order:
        raise HTTPException(status_code=409, detail="Order with given id already exists!")
    order_id = await db_manager.createOrder(request)
    response = {
        'id': order_id,
        **request.dict()
    }
    return response

@orders.put('/orders/{id}', response_model=OrderOut)
async def updateOrder(id: int, request: OrderIn):
    order = await db_manager.getOrderById(id)
    if not order:
        raise HTTPException(status_code=404, detail="Order with given id not found!")
    update_data = request.dict(exclude_unset=True)
    order_in_db = OrderIn(**order)
    updated_order = order_in_db.copy(update=update_data)
    return await db_manager.updateOrder(id, updated_order)

@orders.delete('/orders/{id}', response_model=None)
async def deleteOrder(id: int):
    order = await db_manager.getOrderById(id)
    if not order:
        raise HTTPException(status_code=404, detail="Order with given id not found!")
    return await db_manager.deleteOrder(id)