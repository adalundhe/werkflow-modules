from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDeleteConformancePackRequest(BaseModel):
    ConformancePackName: StrictStr
