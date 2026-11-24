from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .data_zone_row_filter import DataZoneRowFilter


class DataZoneRowFilterConfiguration(BaseModel):
    rowFilter: DataZoneRowFilter | None = None
    sensitive: StrictBool | None = None
