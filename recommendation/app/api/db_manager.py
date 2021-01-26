from app.api.models import RecommendationIn, RecommendationOut, RecommendationUpdate
from app.api.db import recommendations, database

async def createRecommendation(request: RecommendationIn):
    query = recommendations.insert().values(**request.dict())
    return await database.execute(query=query)

async def getAllRecommendations():
    query = recommendations.select()
    return await database.fetch_all(query=query)

async def getRecommendationById(id):
    query = recommendations.select(recommendations.c.id==id)
    return await database.fetch_one(query=query)

async def deleteRecommendation(id: int):
    query = recommendations.delete().where(recommendations.c.id==id)
    return await database.execute(query=query)

async def updateRecommendation(id: int, request: RecommendationIn):
    query = (recommendations.update().where(recommendations.c.id==id).values(**request.dict()))
    return await database.execute(query=query)
