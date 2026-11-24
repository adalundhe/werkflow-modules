from __future__ import annotations
from pydantic import BaseModel
from .data_zone_match_rationale_item import DataZoneMatchRationaleItem


class DataZoneGlossaryTermItemAdditionalAttributes(BaseModel):
    matchRationale: list[DataZoneMatchRationaleItem] | None = None
