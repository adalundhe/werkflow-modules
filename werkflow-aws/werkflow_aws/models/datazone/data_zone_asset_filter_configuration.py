from __future__ import annotations
from pydantic import BaseModel
from .data_zone_column_filter_configuration import DataZoneColumnFilterConfiguration
from .data_zone_row_filter_configuration import DataZoneRowFilterConfiguration


class DataZoneAssetFilterConfiguration(BaseModel):
    columnConfiguration: DataZoneColumnFilterConfiguration | None = None
    rowConfiguration: DataZoneRowFilterConfiguration | None = None
