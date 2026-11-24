from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_lookback_window import QuickSightLookbackWindow


class QuickSightIncrementalRefresh(BaseModel):
    LookbackWindow: QuickSightLookbackWindow | None = None
