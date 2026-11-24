from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_incremental_refresh import QuickSightIncrementalRefresh


class QuickSightRefreshConfiguration(BaseModel):
    IncrementalRefresh: QuickSightIncrementalRefresh | None = None
