from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_data_field_bar_series_item import QuickSightDataFieldBarSeriesItem
from .quick_sight_field_bar_series_item import QuickSightFieldBarSeriesItem


class QuickSightBarSeriesItem(BaseModel):
    FieldBarSeriesItem: QuickSightFieldBarSeriesItem | None = None
    DataFieldBarSeriesItem: QuickSightDataFieldBarSeriesItem | None = None
