from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetServiceLinkedRoleDeletionStatusRequest(BaseModel):
    DeletionTaskId: StrictStr
