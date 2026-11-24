from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_metric_definition import ConnectMetricDefinition


class ConnectDescribeMetricResponse(BaseModel):
    Metric: ConnectMetricDefinition | None = None
    ResponseMetadata: dict[str, Any] | None = None
