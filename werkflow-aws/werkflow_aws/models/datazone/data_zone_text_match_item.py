from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_match_offset import DataZoneMatchOffset


class DataZoneTextMatchItem(BaseModel):
    attribute: StrictStr | None = None
    text: StrictStr | None = None
    matchOffsets: list[DataZoneMatchOffset] | None = None
