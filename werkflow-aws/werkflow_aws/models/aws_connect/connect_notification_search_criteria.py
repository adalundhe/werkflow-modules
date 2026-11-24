from __future__ import annotations
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectNotificationSearchCriteria(BaseModel):
    OrConditions: list[ConnectNotificationSearchCriteria] | None = None
    AndConditions: list[ConnectNotificationSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
