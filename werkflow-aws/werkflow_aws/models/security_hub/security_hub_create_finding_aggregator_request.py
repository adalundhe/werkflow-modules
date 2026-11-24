from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubCreateFindingAggregatorRequest(BaseModel):
    RegionLinkingMode: StrictStr
    Regions: list[StrictStr] | None = None
