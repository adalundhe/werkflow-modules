from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISGetActionRequest(BaseModel):
    id: StrictStr
