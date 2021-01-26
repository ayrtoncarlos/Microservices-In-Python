from typing import Optional
from pydantic import BaseModel

class InventoryIn(BaseModel):
    id: int

class InventoryOut(InventoryIn):
    id: int

class InventoryUpdate(InventoryIn):
    id: Optional[int] = None
