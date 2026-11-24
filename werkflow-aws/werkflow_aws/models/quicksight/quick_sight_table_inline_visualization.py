from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_data_bars_options import QuickSightDataBarsOptions
from .quick_sight_sparklines_options import QuickSightSparklinesOptions


class QuickSightTableInlineVisualization(BaseModel):
    DataBars: QuickSightDataBarsOptions | None = None
    Sparklines: QuickSightSparklinesOptions | None = None
