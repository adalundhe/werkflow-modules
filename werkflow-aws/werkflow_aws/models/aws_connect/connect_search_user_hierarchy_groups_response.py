from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_hierarchy_group import ConnectHierarchyGroup


class ConnectSearchUserHierarchyGroupsResponse(BaseModel):
    UserHierarchyGroups: list[ConnectHierarchyGroup] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
