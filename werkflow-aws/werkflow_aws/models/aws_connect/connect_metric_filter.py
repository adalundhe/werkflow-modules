from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .connect_metric_filter_boolean_condition import ConnectMetricFilterBooleanCondition
from .connect_metric_filter_number_condition import ConnectMetricFilterNumberCondition
from .connect_metric_filter_string_condition import ConnectMetricFilterStringCondition


class ConnectMetricFilter(BaseModel):
    MetricFilterKey: StrictStr | None = None
    Negate: StrictBool | None = None
    NumberCondition: ConnectMetricFilterNumberCondition | None = None
    StringCondition: ConnectMetricFilterStringCondition | None = None
    BooleanCondition: ConnectMetricFilterBooleanCondition | None = None
