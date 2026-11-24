from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_metric_calculation import ConnectMetricCalculation


class ConnectCreateMetricRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    MetricCalculation: ConnectMetricCalculation
    Unit: Literal['INTEGER', 'DOUBLE', 'PERCENT', 'SECONDS']
    Status: Literal['PUBLISHED', 'SAVED'] | None = None
    ClientToken: StrictStr | None = None
    Description: StrictStr | None = None
    PositiveTrendIndicator: Literal['POSITIVE', 'NEGATIVE', 'NEUTRAL'] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
