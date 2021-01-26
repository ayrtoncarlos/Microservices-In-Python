from typing import Optional
from pydantic import BaseModel

class RecommendationIn(BaseModel):
    id: int

class RecommendationOut(RecommendationIn):
    id: int

class RecommendationUpdate(RecommendationIn):
    id: Optional[int] = None
