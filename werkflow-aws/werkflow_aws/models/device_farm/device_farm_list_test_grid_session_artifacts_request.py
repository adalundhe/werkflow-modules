from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DeviceFarmListTestGridSessionArtifactsRequest(BaseModel):
    sessionArn: StrictStr
    type: Literal['VIDEO', 'LOG'] | None = None
    maxResult: StrictInt | None = None
    nextToken: StrictStr | None = None
