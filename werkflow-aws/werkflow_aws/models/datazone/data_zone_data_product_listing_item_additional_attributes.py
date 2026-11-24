from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_match_rationale_item import DataZoneMatchRationaleItem


class DataZoneDataProductListingItemAdditionalAttributes(BaseModel):
    forms: StrictStr | None = None
    matchRationale: list[DataZoneMatchRationaleItem] | None = None
