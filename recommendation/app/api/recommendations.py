from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import RecommendationIn, RecommendationOut, RecommendationUpdate
from app.api import db_manager

recommendations = APIRouter()

@recommendations.get('/recommendations', response_model=List[RecommendationOut])
async def getAllRecommendations():
    return await db_manager.getAllRecommendations()

@recommendations.get('/recommendations/{id}', response_model=RecommendationOut)
async def getRecommendationById(id: int):
    recommendation = await db_manager.getRecommendationById(id)
    if not recommendation:
        raise HTTPException(status_code=404, detail="Recommendation with given id not found!")
    return recommendation

@recommendations.post('/recommendations', response_model=RecommendationOut, status_code=201)
async def createRecommendation(request: RecommendationIn):
    recommendation = await db_manager.getRecommendationById(request.id)
    if recommendation:
        raise HTTPException(status_code=409, detail="Recommendation with given id already exists!")
    recommendation_id = await db_manager.createRecommendation(request)
    response = {
        'id': recommendation_id,
        **request.dict()
    }
    return response

@recommendations.put('/recommendations/{id}', response_model=RecommendationOut)
async def updateRecommendation(id: int, request: RecommendationIn):
    recommendation = await db_manager.getRecommendationById(id)
    if not recommendation:
        raise HTTPException(status_code=404, detail="Recommendation with given id not found!")
    update_data = request.dict(exclude_unset=True)
    recommendation_in_db = RecommendationIn(**recommendation)
    updated_recommendation = recommendation_in_db.copy(update=update_data)
    return await db_manager.updateRecommendation(id, updated_recommendation)

@recommendations.delete('/recommendations/{id}', response_model=None)
async def deleteRecommendation(id: int):
    recommendation = await db_manager.getRecommendationById(id)
    if not recommendation:
        raise HTTPException(status_code=404, detail="Recommendation with given id not found!")
    return await db_manager.deleteRecommendation(id)