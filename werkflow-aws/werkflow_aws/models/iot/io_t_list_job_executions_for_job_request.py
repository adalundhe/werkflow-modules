from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListJobExecutionsForJobRequest(BaseModel):
    jobId: StrictStr
    status: Literal['QUEUED', 'IN_PROGRESS', 'SUCCEEDED', 'FAILED', 'TIMED_OUT', 'REJECTED', 'REMOVED', 'CANCELED'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
