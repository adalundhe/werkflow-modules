from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_refresh_configuration import QuickSightRefreshConfiguration
from .quick_sight_refresh_failure_configuration import QuickSightRefreshFailureConfiguration


class QuickSightDataSetRefreshProperties(BaseModel):
    RefreshConfiguration: QuickSightRefreshConfiguration | None = None
    FailureConfiguration: QuickSightRefreshFailureConfiguration | None = None
