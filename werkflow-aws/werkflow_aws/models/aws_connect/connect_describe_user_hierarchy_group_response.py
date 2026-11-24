from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_hierarchy_group import ConnectHierarchyGroup


class ConnectDescribeUserHierarchyGroupResponse(BaseModel):
    HierarchyGroup: ConnectHierarchyGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
