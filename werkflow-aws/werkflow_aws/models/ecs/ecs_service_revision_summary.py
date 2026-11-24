from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ECSServiceRevisionSummary(BaseModel):
    arn: StrictStr | None = None
    requestedTaskCount: StrictInt | None = None
    runningTaskCount: StrictInt | None = None
    pendingTaskCount: StrictInt | None = None
    requestedTestTrafficWeight: StrictFloat | StrictInt | None = None
    requestedProductionTrafficWeight: StrictFloat | StrictInt | None = None
