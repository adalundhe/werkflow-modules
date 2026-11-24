from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_metric_summary import ConnectMetricSummary


class ConnectListMetricsResponse(BaseModel):
    MetricSummaryList: list[ConnectMetricSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
