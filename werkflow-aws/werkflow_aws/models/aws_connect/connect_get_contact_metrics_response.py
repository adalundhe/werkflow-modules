from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_contact_metric_result import ConnectContactMetricResult


class ConnectGetContactMetricsResponse(BaseModel):
    MetricResults: list[ConnectContactMetricResult] | None = None
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
