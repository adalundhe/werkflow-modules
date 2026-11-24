from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUpdateGroupRequest(BaseModel):
    GroupName: StrictStr
    NewPath: StrictStr | None = None
    NewGroupName: StrictStr | None = None
