from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_metric_datapoint import LightsailMetricDatapoint


class LightsailGetContainerServiceMetricDataResponse(BaseModel):
    metricName: StrictStr | None = None
    metricData: list[LightsailMetricDatapoint] | None = None
    ResponseMetadata: dict[str, Any] | None = None
