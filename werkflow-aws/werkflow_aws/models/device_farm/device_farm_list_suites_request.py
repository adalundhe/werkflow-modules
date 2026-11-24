from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmListSuitesRequest(BaseModel):
    arn: StrictStr
    nextToken: StrictStr | None = None
