from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteUserHierarchyGroupRequest(BaseModel):
    HierarchyGroupId: StrictStr
    InstanceId: StrictStr
