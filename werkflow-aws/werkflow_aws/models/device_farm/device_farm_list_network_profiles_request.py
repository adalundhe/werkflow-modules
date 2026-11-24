from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DeviceFarmListNetworkProfilesRequest(BaseModel):
    arn: StrictStr
    type: Literal['CURATED', 'PRIVATE'] | None = None
    nextToken: StrictStr | None = None
