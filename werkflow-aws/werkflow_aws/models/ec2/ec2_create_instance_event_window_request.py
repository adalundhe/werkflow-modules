from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_instance_event_window_time_range_request import EC2InstanceEventWindowTimeRangeRequest
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateInstanceEventWindowRequest(BaseModel):
    DryRun: StrictBool | None = None
    Name: StrictStr | None = None
    TimeRanges: list[EC2InstanceEventWindowTimeRangeRequest] | None = None
    CronExpression: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
