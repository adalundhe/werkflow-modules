from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class DevOpsGuruPerformanceInsightsStat(BaseModel):
    Type: StrictStr | None = None
    Value: StrictFloat | StrictInt | None = None
