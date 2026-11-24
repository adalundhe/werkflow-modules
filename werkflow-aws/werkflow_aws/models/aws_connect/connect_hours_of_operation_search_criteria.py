from __future__ import annotations
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectHoursOfOperationSearchCriteria(BaseModel):
    OrConditions: list[ConnectHoursOfOperationSearchCriteria] | None = None
    AndConditions: list[ConnectHoursOfOperationSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
