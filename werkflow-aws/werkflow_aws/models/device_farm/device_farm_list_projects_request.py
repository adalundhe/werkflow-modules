from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmListProjectsRequest(BaseModel):
    arn: StrictStr | None = None
    nextToken: StrictStr | None = None
