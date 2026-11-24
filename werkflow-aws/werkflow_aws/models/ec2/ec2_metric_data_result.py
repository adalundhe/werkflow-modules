from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_capacity_manager_dimension import EC2CapacityManagerDimension
from .ec2_metric_value import EC2MetricValue


class EC2MetricDataResult(BaseModel):
    Dimension: EC2CapacityManagerDimension | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
    MetricValues: list[EC2MetricValue] | None = None
