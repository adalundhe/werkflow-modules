from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayGetGroupRequest(BaseModel):
    GroupName: StrictStr | None = None
    GroupARN: StrictStr | None = None
