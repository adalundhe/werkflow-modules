from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesAssociateIpGroupsRequest(BaseModel):
    DirectoryId: StrictStr
    GroupIds: list[StrictStr]
