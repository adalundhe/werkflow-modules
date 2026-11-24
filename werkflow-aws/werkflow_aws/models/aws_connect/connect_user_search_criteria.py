from __future__ import annotations
from pydantic import BaseModel
from .connect_hierarchy_group_condition import ConnectHierarchyGroupCondition
from .connect_list_condition import ConnectListCondition
from .connect_string_condition import ConnectStringCondition


class ConnectUserSearchCriteria(BaseModel):
    OrConditions: list[ConnectUserSearchCriteria] | None = None
    AndConditions: list[ConnectUserSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
    ListCondition: ConnectListCondition | None = None
    HierarchyGroupCondition: ConnectHierarchyGroupCondition | None = None
