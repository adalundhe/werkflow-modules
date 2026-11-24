from __future__ import annotations
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectAgentStatusSearchCriteria(BaseModel):
    OrConditions: list[ConnectAgentStatusSearchCriteria] | None = None
    AndConditions: list[ConnectAgentStatusSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
