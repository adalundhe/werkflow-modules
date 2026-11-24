from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchFrontOfQueueJobSummary(BaseModel):
    jobArn: StrictStr | None = None
    earliestTimeAtPosition: StrictInt | None = None
