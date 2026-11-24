from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .data_zone_aggregation_output import DataZoneAggregationOutput
from .data_zone_search_result_item import DataZoneSearchResultItem


class DataZoneSearchListingsResponse(BaseModel):
    items: list[DataZoneSearchResultItem] | None = None
    nextToken: StrictStr | None = None
    totalMatchCount: StrictInt | None = None
    aggregates: list[DataZoneAggregationOutput] | None = None
    ResponseMetadata: dict[str, Any] | None = None
