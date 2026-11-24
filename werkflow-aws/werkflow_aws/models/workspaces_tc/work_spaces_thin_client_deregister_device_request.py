from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WorkSpacesThinClientDeregisterDeviceRequest(BaseModel):
    id: StrictStr
    targetDeviceStatus: Literal['DEREGISTERED', 'ARCHIVED'] | None = None
    clientToken: StrictStr | None = None
