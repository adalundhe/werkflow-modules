from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeUserHierarchyGroupRequest(BaseModel):
    HierarchyGroupId: StrictStr
    InstanceId: StrictStr
