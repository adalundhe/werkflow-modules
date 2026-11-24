from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel
from .ec2_slot_start_time_range_request import EC2SlotStartTimeRangeRequest


class EC2DescribeScheduledInstancesRequest(BaseModel):
    DryRun: StrictBool | None = None
    Filters: list[EC2FilterModel] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    ScheduledInstanceIds: list[StrictStr] | None = None
    SlotStartTimeRange: EC2SlotStartTimeRangeRequest | None = None
