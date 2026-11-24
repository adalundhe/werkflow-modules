from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel
from .ec2_scheduled_instance_recurrence_request import EC2ScheduledInstanceRecurrenceRequest
from .ec2_slot_date_time_range_request import EC2SlotDateTimeRangeRequest


class EC2DescribeScheduledInstanceAvailabilityRequest(BaseModel):
    FirstSlotStartTimeRange: EC2SlotDateTimeRangeRequest
    Recurrence: EC2ScheduledInstanceRecurrenceRequest
    DryRun: StrictBool | None = None
    Filters: list[EC2FilterModel] | None = None
    MaxResults: StrictInt | None = None
    MaxSlotDurationInHours: StrictInt | None = None
    MinSlotDurationInHours: StrictInt | None = None
    NextToken: StrictStr | None = None
