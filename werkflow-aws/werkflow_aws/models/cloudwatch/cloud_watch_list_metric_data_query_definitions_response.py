from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_metric_data_query_definition_summary import CloudWatchMetricDataQueryDefinitionSummary


class CloudWatchListMetricDataQueryDefinitionsResponse(BaseModel):
    Items: list[CloudWatchMetricDataQueryDefinitionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
