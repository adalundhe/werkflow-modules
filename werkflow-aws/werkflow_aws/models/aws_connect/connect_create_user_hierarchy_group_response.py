from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateUserHierarchyGroupResponse(BaseModel):
    HierarchyGroupId: StrictStr | None = None
    HierarchyGroupArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
