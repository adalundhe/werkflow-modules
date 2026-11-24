from __future__ import annotations
from pydantic import BaseModel, StrictBool


class XRayInsightsConfiguration(BaseModel):
    InsightsEnabled: StrictBool | None = None
    NotificationsEnabled: StrictBool | None = None
