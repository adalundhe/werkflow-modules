from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2AnalyticsConfig(BaseModel):
    Mode: StrictStr | None = None
