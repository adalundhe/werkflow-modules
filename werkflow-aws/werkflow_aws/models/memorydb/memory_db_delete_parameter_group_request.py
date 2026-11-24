from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBDeleteParameterGroupRequest(BaseModel):
    ParameterGroupName: StrictStr
