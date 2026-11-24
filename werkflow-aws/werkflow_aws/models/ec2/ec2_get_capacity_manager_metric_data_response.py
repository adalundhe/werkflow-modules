from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_metric_data_result import EC2MetricDataResult


class EC2GetCapacityManagerMetricDataResponse(BaseModel):
    MetricDataResults: list[EC2MetricDataResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
