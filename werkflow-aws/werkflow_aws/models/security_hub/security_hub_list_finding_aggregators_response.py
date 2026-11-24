from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_finding_aggregator import SecurityHubFindingAggregator


class SecurityHubListFindingAggregatorsResponse(BaseModel):
    FindingAggregators: list[SecurityHubFindingAggregator] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
