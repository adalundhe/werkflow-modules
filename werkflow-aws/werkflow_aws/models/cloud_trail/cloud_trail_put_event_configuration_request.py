from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cloud_trail_aggregation_configuration import CloudTrailAggregationConfiguration
from .cloud_trail_context_key_selector import CloudTrailContextKeySelector


class CloudTrailPutEventConfigurationRequest(BaseModel):
    TrailName: StrictStr | None = None
    EventDataStore: StrictStr | None = None
    MaxEventSize: Literal['Standard', 'Large'] | None = None
    ContextKeySelectors: list[CloudTrailContextKeySelector] | None = None
    AggregationConfigurations: list[CloudTrailAggregationConfiguration] | None = None
