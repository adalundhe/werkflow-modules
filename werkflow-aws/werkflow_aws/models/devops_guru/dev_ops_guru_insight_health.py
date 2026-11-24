from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DevOpsGuruInsightHealth(BaseModel):
    OpenProactiveInsights: StrictInt | None = None
    OpenReactiveInsights: StrictInt | None = None
    MeanTimeToRecoverInMilliseconds: StrictInt | None = None
