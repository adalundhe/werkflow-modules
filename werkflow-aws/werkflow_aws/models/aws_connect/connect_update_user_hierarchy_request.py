from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateUserHierarchyRequest(BaseModel):
    UserId: StrictStr
    InstanceId: StrictStr
    HierarchyGroupId: StrictStr | None = None
