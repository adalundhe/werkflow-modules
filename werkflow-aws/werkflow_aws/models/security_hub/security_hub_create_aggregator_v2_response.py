from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SecurityHubCreateAggregatorV2Response(BaseModel):
    AggregatorV2Arn: StrictStr | None = None
    AggregationRegion: StrictStr | None = None
    RegionLinkingMode: StrictStr | None = None
    LinkedRegions: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
