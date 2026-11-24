from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraMemberUser(BaseModel):
    UserId: StrictStr
