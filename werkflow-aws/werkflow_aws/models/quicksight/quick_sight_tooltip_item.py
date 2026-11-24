from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_column_tooltip_item import QuickSightColumnTooltipItem
from .quick_sight_field_tooltip_item import QuickSightFieldTooltipItem


class QuickSightTooltipItem(BaseModel):
    FieldTooltipItem: QuickSightFieldTooltipItem | None = None
    ColumnTooltipItem: QuickSightColumnTooltipItem | None = None
