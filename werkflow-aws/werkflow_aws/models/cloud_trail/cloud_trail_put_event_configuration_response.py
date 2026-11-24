from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_aggregation_configuration import CloudTrailAggregationConfiguration
from .cloud_trail_context_key_selector import CloudTrailContextKeySelector


class CloudTrailPutEventConfigurationResponse(BaseModel):
    TrailARN: StrictStr | None = None
    EventDataStoreArn: StrictStr | None = None
    MaxEventSize: StrictStr | None = None
    ContextKeySelectors: list[CloudTrailContextKeySelector] | None = None
    AggregationConfigurations: list[CloudTrailAggregationConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
