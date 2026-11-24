from __future__ import annotations
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectRoutingProfileSearchCriteria(BaseModel):
    OrConditions: list[ConnectRoutingProfileSearchCriteria] | None = None
    AndConditions: list[ConnectRoutingProfileSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
