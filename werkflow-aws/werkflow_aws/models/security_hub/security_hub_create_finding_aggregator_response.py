from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SecurityHubCreateFindingAggregatorResponse(BaseModel):
    FindingAggregatorArn: StrictStr | None = None
    FindingAggregationRegion: StrictStr | None = None
    RegionLinkingMode: StrictStr | None = None
    Regions: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
