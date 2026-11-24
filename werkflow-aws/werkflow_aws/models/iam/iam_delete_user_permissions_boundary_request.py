from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteUserPermissionsBoundaryRequest(BaseModel):
    UserName: StrictStr
