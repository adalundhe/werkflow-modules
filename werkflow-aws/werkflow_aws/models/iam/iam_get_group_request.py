from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMGetGroupRequest(BaseModel):
    GroupName: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
