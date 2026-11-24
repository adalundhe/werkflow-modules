from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDisassociateIpGroupsRequest(BaseModel):
    DirectoryId: StrictStr
    GroupIds: list[StrictStr]
