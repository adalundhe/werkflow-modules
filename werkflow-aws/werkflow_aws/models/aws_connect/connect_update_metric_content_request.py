from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_metric_calculation import ConnectMetricCalculation


class ConnectUpdateMetricContentRequest(BaseModel):
    InstanceId: StrictStr
    MetricId: StrictStr
    MetricCalculation: ConnectMetricCalculation | None = None
    Unit: Literal['INTEGER', 'DOUBLE', 'PERCENT', 'SECONDS'] | None = None
    PositiveTrendIndicator: Literal['POSITIVE', 'NEGATIVE', 'NEUTRAL'] | None = None
