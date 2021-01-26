from typing import Optional
from pydantic import BaseModel

class OrderIn(BaseModel):
    id: int

class OrderOut(OrderIn):
    id: int

class OrderUpdate(OrderIn):
    id: Optional[int] = None
