from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubUpdateFindingAggregatorRequest(BaseModel):
    FindingAggregatorArn: StrictStr
    RegionLinkingMode: StrictStr
    Regions: list[StrictStr] | None = None
