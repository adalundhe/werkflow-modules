from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_refresh_failure_email_alert import QuickSightRefreshFailureEmailAlert


class QuickSightRefreshFailureConfiguration(BaseModel):
    EmailAlert: QuickSightRefreshFailureEmailAlert | None = None
