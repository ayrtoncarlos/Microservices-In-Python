from fastapi import FastAPI
from app.api.inventories import inventories
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(openapi_url='/api/v1/inventories/openapi.json', docs_url='/api/v1/inventories/docs')

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(inventories, prefix='/api/v1/inventories', tags=['inventories'])