from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_aggregation_authorization import ConfigServiceAggregationAuthorization


class ConfigServicePutAggregationAuthorizationResponse(BaseModel):
    AggregationAuthorization: ConfigServiceAggregationAuthorization | None = None
    ResponseMetadata: dict[str, Any] | None = None
