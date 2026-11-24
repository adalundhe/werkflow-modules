from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_field_based_tooltip import QuickSightFieldBasedTooltip
from .quick_sight_sheet_tooltip import QuickSightSheetTooltip


class QuickSightTooltipOptions(BaseModel):
    TooltipVisibility: StrictStr | None = None
    SelectedTooltipType: StrictStr | None = None
    FieldBasedTooltip: QuickSightFieldBasedTooltip | None = None
    SheetTooltip: QuickSightSheetTooltip | None = None
