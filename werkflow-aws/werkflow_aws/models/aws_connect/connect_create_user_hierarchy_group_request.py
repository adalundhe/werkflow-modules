from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCreateUserHierarchyGroupRequest(BaseModel):
    Name: StrictStr
    InstanceId: StrictStr
    ParentGroupId: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
