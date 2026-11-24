from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowGoogleAnalyticsSourceProperties(BaseModel):
    object: StrictStr | None = None
