from __future__ import annotations
from pydantic import BaseModel
from .connect_boolean_condition import ConnectBooleanCondition
from .connect_date_time_condition import ConnectDateTimeCondition
from .connect_number_condition import ConnectNumberCondition
from .connect_string_condition import ConnectStringCondition


class ConnectEvaluationFormSearchCriteria(BaseModel):
    OrConditions: list[ConnectEvaluationFormSearchCriteria] | None = None
    AndConditions: list[ConnectEvaluationFormSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
    NumberCondition: ConnectNumberCondition | None = None
    BooleanCondition: ConnectBooleanCondition | None = None
    DateTimeCondition: ConnectDateTimeCondition | None = None
