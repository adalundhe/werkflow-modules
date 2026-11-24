from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_capacity_manager_condition import EC2CapacityManagerCondition


class EC2GetCapacityManagerMetricDimensionsRequest(BaseModel):
    GroupBy: list[Literal['resource-region', 'availability-zone-id', 'account-id', 'account-name', 'instance-family', 'instance-type', 'instance-platform', 'reservation-arn', 'reservation-id', 'reservation-type', 'reservation-create-timestamp', 'reservation-start-timestamp', 'reservation-end-timestamp', 'reservation-end-date-type', 'tenancy', 'reservation-state', 'reservation-instance-match-criteria', 'reservation-unused-financial-owner']]
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
    MetricNames: list[StrictStr]
    FilterBy: list[EC2CapacityManagerCondition] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    DryRun: StrictBool | None = None
