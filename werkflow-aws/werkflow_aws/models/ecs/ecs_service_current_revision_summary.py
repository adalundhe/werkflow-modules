from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSServiceCurrentRevisionSummary(BaseModel):
    arn: StrictStr | None = None
    requestedTaskCount: StrictInt | None = None
    runningTaskCount: StrictInt | None = None
    pendingTaskCount: StrictInt | None = None
