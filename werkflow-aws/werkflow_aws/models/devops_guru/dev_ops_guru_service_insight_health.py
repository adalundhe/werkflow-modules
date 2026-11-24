from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DevOpsGuruServiceInsightHealth(BaseModel):
    OpenProactiveInsights: StrictInt | None = None
    OpenReactiveInsights: StrictInt | None = None
