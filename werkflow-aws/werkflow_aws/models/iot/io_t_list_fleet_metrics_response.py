from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_fleet_metric_name_and_arn import IoTFleetMetricNameAndArn


class IoTListFleetMetricsResponse(BaseModel):
    fleetMetrics: list[IoTFleetMetricNameAndArn] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
