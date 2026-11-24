from __future__ import annotations
from pydantic import BaseModel
from .data_zone_form_output import DataZoneFormOutput
from .data_zone_match_rationale_item import DataZoneMatchRationaleItem
from .data_zone_time_series_data_point_summary_form_output import DataZoneTimeSeriesDataPointSummaryFormOutput


class DataZoneAssetItemAdditionalAttributes(BaseModel):
    formsOutput: list[DataZoneFormOutput] | None = None
    readOnlyFormsOutput: list[DataZoneFormOutput] | None = None
    latestTimeSeriesDataPointFormsOutput: list[DataZoneTimeSeriesDataPointSummaryFormOutput] | None = None
    matchRationale: list[DataZoneMatchRationaleItem] | None = None
