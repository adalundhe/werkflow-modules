from __future__ import annotations
from pydantic import BaseModel
from .connect_boolean_condition import ConnectBooleanCondition
from .connect_string_condition import ConnectStringCondition


class ConnectMetricSearchCriteria(BaseModel):
    OrConditions: list[ConnectMetricSearchCriteria] | None = None
    AndConditions: list[ConnectMetricSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
    BooleanCondition: ConnectBooleanCondition | None = None
