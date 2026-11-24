from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMPutUserPermissionsBoundaryRequest(BaseModel):
    UserName: StrictStr
    PermissionsBoundary: StrictStr
