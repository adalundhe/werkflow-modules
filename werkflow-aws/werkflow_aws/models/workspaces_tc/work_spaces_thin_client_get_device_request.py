from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesThinClientGetDeviceRequest(BaseModel):
    id: StrictStr
