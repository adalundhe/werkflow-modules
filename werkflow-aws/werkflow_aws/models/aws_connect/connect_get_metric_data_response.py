from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_historical_metric_result import ConnectHistoricalMetricResult


class ConnectGetMetricDataResponse(BaseModel):
    NextToken: StrictStr | None = None
    MetricResults: list[ConnectHistoricalMetricResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
