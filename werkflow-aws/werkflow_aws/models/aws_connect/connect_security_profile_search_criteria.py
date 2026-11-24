from __future__ import annotations
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectSecurityProfileSearchCriteria(BaseModel):
    OrConditions: list[ConnectSecurityProfileSearchCriteria] | None = None
    AndConditions: list[ConnectSecurityProfileSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
