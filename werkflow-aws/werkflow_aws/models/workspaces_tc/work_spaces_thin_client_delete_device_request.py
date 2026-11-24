from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesThinClientDeleteDeviceRequest(BaseModel):
    id: StrictStr
    clientToken: StrictStr | None = None
