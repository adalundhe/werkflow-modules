from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConfigServiceScopeConfiguration(BaseModel):
    scopeType: StrictStr | None = None
    scopeValues: list[StrictStr] | None = None
    allRegions: StrictBool | None = None
    includedRegions: list[StrictStr] | None = None
