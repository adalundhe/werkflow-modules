from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDashboardAttributes(BaseModel):
    EngagementMetrics: StrictStr | None = None
