from __future__ import annotations
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectUserHierarchyGroupSearchCriteria(BaseModel):
    OrConditions: list[ConnectUserHierarchyGroupSearchCriteria] | None = None
    AndConditions: list[ConnectUserHierarchyGroupSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
