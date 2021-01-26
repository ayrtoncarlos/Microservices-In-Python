from typing import Optional
from pydantic import BaseModel

class ShippingIn(BaseModel):
    id: int

class ShippingOut(ShippingIn):
    id: int

class ShippingUpdate(ShippingIn):
    id: Optional[int] = None
