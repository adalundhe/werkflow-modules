from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_scheduled_instance_recurrence import EC2ScheduledInstanceRecurrence


class EC2ScheduledInstance(BaseModel):
    AvailabilityZone: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    HourlyPrice: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    InstanceType: StrictStr | None = None
    NetworkPlatform: StrictStr | None = None
    NextSlotStartTime: datetime.datetime | StrictStr | None = None
    Platform: StrictStr | None = None
    PreviousSlotEndTime: datetime.datetime | StrictStr | None = None
    Recurrence: EC2ScheduledInstanceRecurrence | None = None
    ScheduledInstanceId: StrictStr | None = None
    SlotDurationInHours: StrictInt | None = None
    TermEndDate: datetime.datetime | StrictStr | None = None
    TermStartDate: datetime.datetime | StrictStr | None = None
    TotalScheduledInstanceHours: StrictInt | None = None
