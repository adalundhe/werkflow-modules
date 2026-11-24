from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmListUploadsRequest(BaseModel):
    arn: StrictStr
    type: StrictStr | None = None
    nextToken: StrictStr | None = None
