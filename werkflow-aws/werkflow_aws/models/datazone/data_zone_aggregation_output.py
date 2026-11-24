from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_aggregation_output_item import DataZoneAggregationOutputItem


class DataZoneAggregationOutput(BaseModel):
    attribute: StrictStr | None = None
    displayValue: StrictStr | None = None
    items: list[DataZoneAggregationOutputItem] | None = None
