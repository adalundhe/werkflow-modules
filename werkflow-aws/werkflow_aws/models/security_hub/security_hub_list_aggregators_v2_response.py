from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_aggregator_v2 import SecurityHubAggregatorV2


class SecurityHubListAggregatorsV2Response(BaseModel):
    AggregatorsV2: list[SecurityHubAggregatorV2] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
