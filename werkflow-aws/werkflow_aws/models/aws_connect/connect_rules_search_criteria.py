from __future__ import annotations
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectRulesSearchCriteria(BaseModel):
    OrConditions: list[ConnectRulesSearchCriteria] | None = None
    AndConditions: list[ConnectRulesSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
