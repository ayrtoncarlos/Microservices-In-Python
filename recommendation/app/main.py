from fastapi import FastAPI
from app.api.recommendations import recommendations
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(openapi_url='/api/v1/recommendations/openapi.json', docs_url='/api/v1/recommendations/docs')

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(recommendations, prefix='/api/v1/recommendations', tags=['recommendations'])