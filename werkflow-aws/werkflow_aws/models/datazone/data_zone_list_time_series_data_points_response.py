from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_time_series_data_point_summary_form_output import DataZoneTimeSeriesDataPointSummaryFormOutput


class DataZoneListTimeSeriesDataPointsResponse(BaseModel):
    items: list[DataZoneTimeSeriesDataPointSummaryFormOutput] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
