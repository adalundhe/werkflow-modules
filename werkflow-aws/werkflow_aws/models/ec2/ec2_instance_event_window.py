from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_instance_event_window_association_target import EC2InstanceEventWindowAssociationTarget
from .ec2_instance_event_window_time_range import EC2InstanceEventWindowTimeRange
from .ec2_tag_model import EC2TagModel


class EC2InstanceEventWindow(BaseModel):
    InstanceEventWindowId: StrictStr | None = None
    TimeRanges: list[EC2InstanceEventWindowTimeRange] | None = None
    Name: StrictStr | None = None
    CronExpression: StrictStr | None = None
    AssociationTarget: EC2InstanceEventWindowAssociationTarget | None = None
    State: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
