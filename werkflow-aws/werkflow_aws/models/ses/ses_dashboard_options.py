from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDashboardOptions(BaseModel):
    EngagementMetrics: StrictStr | None = None
