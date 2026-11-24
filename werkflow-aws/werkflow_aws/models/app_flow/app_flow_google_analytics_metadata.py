from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowGoogleAnalyticsMetadata(BaseModel):
    oAuthScopes: list[StrictStr] | None = None
