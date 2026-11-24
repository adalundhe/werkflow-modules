from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_aggregated_source_status import ConfigServiceAggregatedSourceStatus


class ConfigServiceDescribeConfigurationAggregatorSourcesStatusResponse(BaseModel):
    AggregatedSourceStatusList: list[ConfigServiceAggregatedSourceStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
