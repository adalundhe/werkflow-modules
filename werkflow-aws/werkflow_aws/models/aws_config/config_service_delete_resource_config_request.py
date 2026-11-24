from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDeleteResourceConfigRequest(BaseModel):
    ResourceType: StrictStr
    ResourceId: StrictStr
