from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBEngineVersionInfo(BaseModel):
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    EnginePatchVersion: StrictStr | None = None
    ParameterGroupFamily: StrictStr | None = None
