from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_metric_definition import ConnectMetricDefinition


class ConnectSearchMetricsResponse(BaseModel):
    Metrics: list[ConnectMetricDefinition] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
