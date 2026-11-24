from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_scheduled_instance_recurrence import EC2ScheduledInstanceRecurrence


class EC2ScheduledInstanceAvailability(BaseModel):
    AvailabilityZone: StrictStr | None = None
    AvailableInstanceCount: StrictInt | None = None
    FirstSlotStartTime: datetime.datetime | StrictStr | None = None
    HourlyPrice: StrictStr | None = None
    InstanceType: StrictStr | None = None
    MaxTermDurationInDays: StrictInt | None = None
    MinTermDurationInDays: StrictInt | None = None
    NetworkPlatform: StrictStr | None = None
    Platform: StrictStr | None = None
    PurchaseToken: StrictStr | None = None
    Recurrence: EC2ScheduledInstanceRecurrence | None = None
    SlotDurationInHours: StrictInt | None = None
    TotalScheduledInstanceHours: StrictInt | None = None
