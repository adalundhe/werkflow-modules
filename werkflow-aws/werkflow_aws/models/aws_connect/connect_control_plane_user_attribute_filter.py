from __future__ import annotations
from pydantic import BaseModel
from .connect_attribute_and_condition import ConnectAttributeAndCondition
from .connect_hierarchy_group_condition import ConnectHierarchyGroupCondition
from .connect_tag_condition import ConnectTagCondition


class ConnectControlPlaneUserAttributeFilter(BaseModel):
    OrConditions: list[ConnectAttributeAndCondition] | None = None
    AndCondition: ConnectAttributeAndCondition | None = None
    TagCondition: ConnectTagCondition | None = None
    HierarchyGroupCondition: ConnectHierarchyGroupCondition | None = None
