from __future__ import annotations
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectWorkspaceSearchCriteria(BaseModel):
    OrConditions: list[ConnectWorkspaceSearchCriteria] | None = None
    AndConditions: list[ConnectWorkspaceSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
