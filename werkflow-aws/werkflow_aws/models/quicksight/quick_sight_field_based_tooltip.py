from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_tooltip_item import QuickSightTooltipItem


class QuickSightFieldBasedTooltip(BaseModel):
    AggregationVisibility: StrictStr | None = None
    TooltipTitleType: StrictStr | None = None
    TooltipFields: list[QuickSightTooltipItem] | None = None
