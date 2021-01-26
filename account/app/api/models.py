from typing import Optional
from pydantic import BaseModel

class AccountIn(BaseModel):
    id: int
    name: str

class AccountOut(AccountIn):
    id: int

class AccountUpdate(AccountIn):
    id: Optional[int] = None
    name: Optional[str] = None
