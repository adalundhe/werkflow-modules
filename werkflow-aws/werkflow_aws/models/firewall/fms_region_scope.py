from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FMSRegionScope(BaseModel):
    Regions: list[StrictStr] | None = None
    AllRegionsEnabled: StrictBool | None = None
