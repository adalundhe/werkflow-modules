from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmListRemoteAccessSessionsRequest(BaseModel):
    arn: StrictStr
    nextToken: StrictStr | None = None
