from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_metric_point import EC2MetricPoint


class EC2DataResponse(BaseModel):
    Id: StrictStr | None = None
    Source: StrictStr | None = None
    Destination: StrictStr | None = None
    Metric: StrictStr | None = None
    Statistic: StrictStr | None = None
    Period: StrictStr | None = None
    MetricPoints: list[EC2MetricPoint] | None = None
