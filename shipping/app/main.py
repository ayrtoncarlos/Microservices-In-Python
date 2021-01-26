from fastapi import FastAPI
from app.api.shipments import shipments
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(openapi_url='/api/v1/shipments/openapi.json', docs_url='/api/v1/shipments/docs')

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(shipments, prefix='/api/v1/shipments', tags=['shipments'])