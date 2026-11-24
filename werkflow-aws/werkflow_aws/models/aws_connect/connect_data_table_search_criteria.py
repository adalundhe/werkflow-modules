from __future__ import annotations
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectDataTableSearchCriteria(BaseModel):
    OrConditions: list[ConnectDataTableSearchCriteria] | None = None
    AndConditions: list[ConnectDataTableSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
