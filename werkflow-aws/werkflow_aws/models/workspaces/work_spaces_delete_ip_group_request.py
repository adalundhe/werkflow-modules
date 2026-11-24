from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDeleteIpGroupRequest(BaseModel):
    GroupId: StrictStr
