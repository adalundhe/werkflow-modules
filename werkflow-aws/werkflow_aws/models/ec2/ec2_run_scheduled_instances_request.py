from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_scheduled_instances_launch_specification import EC2ScheduledInstancesLaunchSpecification


class EC2RunScheduledInstancesRequest(BaseModel):
    LaunchSpecification: EC2ScheduledInstancesLaunchSpecification
    ScheduledInstanceId: StrictStr
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    InstanceCount: StrictInt | None = None
