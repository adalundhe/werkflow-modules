from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubUpdateAggregatorV2Request(BaseModel):
    AggregatorV2Arn: StrictStr
    RegionLinkingMode: StrictStr
    LinkedRegions: list[StrictStr] | None = None
