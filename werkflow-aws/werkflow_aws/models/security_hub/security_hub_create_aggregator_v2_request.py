from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubCreateAggregatorV2Request(BaseModel):
    RegionLinkingMode: StrictStr
    LinkedRegions: list[StrictStr] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ClientToken: StrictStr | None = None
