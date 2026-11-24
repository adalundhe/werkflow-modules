from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheDeleteUserRequest(BaseModel):
    UserId: StrictStr
