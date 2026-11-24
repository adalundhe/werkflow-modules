from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DeviceFarmListTestGridSessionActionsRequest(BaseModel):
    sessionArn: StrictStr
    maxResult: StrictInt | None = None
    nextToken: StrictStr | None = None
