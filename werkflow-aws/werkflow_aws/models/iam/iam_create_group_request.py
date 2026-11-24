from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMCreateGroupRequest(BaseModel):
    GroupName: StrictStr
    Path: StrictStr | None = None
