from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateUserHierarchyGroupNameRequest(BaseModel):
    Name: StrictStr
    HierarchyGroupId: StrictStr
    InstanceId: StrictStr
