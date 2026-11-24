from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_scheduled_instances_ebs import EC2ScheduledInstancesEbs


class EC2ScheduledInstancesBlockDeviceMapping(BaseModel):
    DeviceName: StrictStr | None = None
    Ebs: EC2ScheduledInstancesEbs | None = None
    NoDevice: StrictStr | None = None
    VirtualName: StrictStr | None = None
