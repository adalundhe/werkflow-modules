from __future__ import annotations
from pydantic import BaseModel
from .connect_date_condition import ConnectDateCondition
from .connect_string_condition import ConnectStringCondition


class ConnectHoursOfOperationOverrideSearchCriteria(BaseModel):
    OrConditions: list[ConnectHoursOfOperationOverrideSearchCriteria] | None = None
    AndConditions: list[ConnectHoursOfOperationOverrideSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
    DateCondition: ConnectDateCondition | None = None
