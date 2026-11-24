from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmListJobsRequest(BaseModel):
    arn: StrictStr
    nextToken: StrictStr | None = None
