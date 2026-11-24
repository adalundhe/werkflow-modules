from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_asset_filter_summary import DataZoneAssetFilterSummary


class DataZoneListAssetFiltersResponse(BaseModel):
    items: list[DataZoneAssetFilterSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
