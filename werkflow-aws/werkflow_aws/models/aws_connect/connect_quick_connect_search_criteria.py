from __future__ import annotations
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectQuickConnectSearchCriteria(BaseModel):
    OrConditions: list[ConnectQuickConnectSearchCriteria] | None = None
    AndConditions: list[ConnectQuickConnectSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
