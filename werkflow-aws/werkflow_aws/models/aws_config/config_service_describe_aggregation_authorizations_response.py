from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_aggregation_authorization import ConfigServiceAggregationAuthorization


class ConfigServiceDescribeAggregationAuthorizationsResponse(BaseModel):
    AggregationAuthorizations: list[ConfigServiceAggregationAuthorization] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
