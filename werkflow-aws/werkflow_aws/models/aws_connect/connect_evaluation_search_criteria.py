from __future__ import annotations
from pydantic import BaseModel
from .connect_boolean_condition import ConnectBooleanCondition
from .connect_date_time_condition import ConnectDateTimeCondition
from .connect_decimal_condition import ConnectDecimalCondition
from .connect_number_condition import ConnectNumberCondition
from .connect_string_condition import ConnectStringCondition


class ConnectEvaluationSearchCriteria(BaseModel):
    OrConditions: list[ConnectEvaluationSearchCriteria] | None = None
    AndConditions: list[ConnectEvaluationSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
    NumberCondition: ConnectNumberCondition | None = None
    BooleanCondition: ConnectBooleanCondition | None = None
    DateTimeCondition: ConnectDateTimeCondition | None = None
    DecimalCondition: ConnectDecimalCondition | None = None
