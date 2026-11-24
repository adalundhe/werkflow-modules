from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class DevOpsGuruPerformanceInsightsReferenceScalar(BaseModel):
    Value: StrictFloat | StrictInt | None = None
