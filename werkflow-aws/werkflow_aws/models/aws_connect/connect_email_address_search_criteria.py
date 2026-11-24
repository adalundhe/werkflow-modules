from __future__ import annotations
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectEmailAddressSearchCriteria(BaseModel):
    OrConditions: list[ConnectEmailAddressSearchCriteria] | None = None
    AndConditions: list[ConnectEmailAddressSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
