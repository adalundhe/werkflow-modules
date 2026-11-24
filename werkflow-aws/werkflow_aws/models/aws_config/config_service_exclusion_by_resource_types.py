from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceExclusionByResourceTypes(BaseModel):
    resourceTypes: list[StrictStr] | None = None
