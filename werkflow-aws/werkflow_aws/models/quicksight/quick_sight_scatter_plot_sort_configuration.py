from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_items_limit_configuration import QuickSightItemsLimitConfiguration


class QuickSightScatterPlotSortConfiguration(BaseModel):
    ScatterPlotLimitConfiguration: QuickSightItemsLimitConfiguration | None = None
