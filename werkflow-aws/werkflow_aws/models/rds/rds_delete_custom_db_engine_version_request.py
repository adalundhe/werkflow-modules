from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDeleteCustomDBEngineVersionRequest(BaseModel):
    Engine: StrictStr
    EngineVersion: StrictStr
