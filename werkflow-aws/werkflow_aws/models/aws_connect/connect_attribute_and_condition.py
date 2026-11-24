from __future__ import annotations
from pydantic import BaseModel
from .connect_hierarchy_group_condition import ConnectHierarchyGroupCondition
from .connect_tag_condition import ConnectTagCondition


class ConnectAttributeAndCondition(BaseModel):
    TagConditions: list[ConnectTagCondition] | None = None
    HierarchyGroupCondition: ConnectHierarchyGroupCondition | None = None
