from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeUserHierarchyStructureRequest(BaseModel):
    InstanceId: StrictStr
