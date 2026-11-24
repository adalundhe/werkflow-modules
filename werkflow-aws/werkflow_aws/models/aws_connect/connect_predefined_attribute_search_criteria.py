from __future__ import annotations
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectPredefinedAttributeSearchCriteria(BaseModel):
    OrConditions: list[ConnectPredefinedAttributeSearchCriteria] | None = None
    AndConditions: list[ConnectPredefinedAttributeSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
