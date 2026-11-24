from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmListUniqueProblemsRequest(BaseModel):
    arn: StrictStr
    nextToken: StrictStr | None = None
