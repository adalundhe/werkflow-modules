from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmListRunsRequest(BaseModel):
    arn: StrictStr
    nextToken: StrictStr | None = None
