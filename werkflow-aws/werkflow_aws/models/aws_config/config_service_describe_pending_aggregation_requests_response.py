from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_pending_aggregation_request import ConfigServicePendingAggregationRequest


class ConfigServiceDescribePendingAggregationRequestsResponse(BaseModel):
    PendingAggregationRequests: list[ConfigServicePendingAggregationRequest] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
