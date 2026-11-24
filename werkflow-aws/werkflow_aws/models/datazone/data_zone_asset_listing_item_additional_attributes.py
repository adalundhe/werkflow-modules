from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_match_rationale_item import DataZoneMatchRationaleItem
from .data_zone_time_series_data_point_summary_form_output import DataZoneTimeSeriesDataPointSummaryFormOutput


class DataZoneAssetListingItemAdditionalAttributes(BaseModel):
    forms: StrictStr | None = None
    matchRationale: list[DataZoneMatchRationaleItem] | None = None
    latestTimeSeriesDataPointForms: list[DataZoneTimeSeriesDataPointSummaryFormOutput] | None = None
