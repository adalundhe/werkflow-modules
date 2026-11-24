from __future__ import annotations
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectWorkspaceAssociationSearchCriteria(BaseModel):
    OrConditions: list[ConnectWorkspaceAssociationSearchCriteria] | None = None
    AndConditions: list[ConnectWorkspaceAssociationSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
