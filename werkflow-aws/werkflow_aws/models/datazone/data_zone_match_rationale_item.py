from __future__ import annotations
from pydantic import BaseModel
from .data_zone_text_match_item import DataZoneTextMatchItem


class DataZoneMatchRationaleItem(BaseModel):
    textMatches: list[DataZoneTextMatchItem] | None = None
