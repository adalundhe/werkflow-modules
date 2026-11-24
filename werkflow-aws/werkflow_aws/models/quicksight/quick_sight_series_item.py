from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_data_field_series_item import QuickSightDataFieldSeriesItem
from .quick_sight_field_series_item import QuickSightFieldSeriesItem


class QuickSightSeriesItem(BaseModel):
    FieldSeriesItem: QuickSightFieldSeriesItem | None = None
    DataFieldSeriesItem: QuickSightDataFieldSeriesItem | None = None
