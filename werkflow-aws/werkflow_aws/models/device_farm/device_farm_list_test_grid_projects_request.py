from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DeviceFarmListTestGridProjectsRequest(BaseModel):
    maxResult: StrictInt | None = None
    nextToken: StrictStr | None = None
