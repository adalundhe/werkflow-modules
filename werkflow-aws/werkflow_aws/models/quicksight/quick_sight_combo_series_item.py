from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_data_field_combo_series_item import QuickSightDataFieldComboSeriesItem
from .quick_sight_field_combo_series_item import QuickSightFieldComboSeriesItem


class QuickSightComboSeriesItem(BaseModel):
    FieldComboSeriesItem: QuickSightFieldComboSeriesItem | None = None
    DataFieldComboSeriesItem: QuickSightDataFieldComboSeriesItem | None = None
