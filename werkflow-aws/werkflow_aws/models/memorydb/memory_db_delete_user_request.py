from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBDeleteUserRequest(BaseModel):
    UserName: StrictStr
