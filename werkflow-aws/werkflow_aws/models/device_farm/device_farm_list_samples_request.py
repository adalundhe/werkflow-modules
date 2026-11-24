from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmListSamplesRequest(BaseModel):
    arn: StrictStr
    nextToken: StrictStr | None = None
