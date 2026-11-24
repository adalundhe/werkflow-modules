from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_launch_specification import EC2LaunchSpecification
from .ec2_spot_instance_state_fault import EC2SpotInstanceStateFault
from .ec2_spot_instance_status import EC2SpotInstanceStatus
from .ec2_tag_model import EC2TagModel


class EC2SpotInstanceRequest(BaseModel):
    ActualBlockHourlyPrice: StrictStr | None = None
    AvailabilityZoneGroup: StrictStr | None = None
    BlockDurationMinutes: StrictInt | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    Fault: EC2SpotInstanceStateFault | None = None
    InstanceId: StrictStr | None = None
    LaunchGroup: StrictStr | None = None
    LaunchSpecification: EC2LaunchSpecification | None = None
    LaunchedAvailabilityZone: StrictStr | None = None
    LaunchedAvailabilityZoneId: StrictStr | None = None
    ProductDescription: StrictStr | None = None
    SpotInstanceRequestId: StrictStr | None = None
    SpotPrice: StrictStr | None = None
    State: StrictStr | None = None
    Status: EC2SpotInstanceStatus | None = None
    Tags: list[EC2TagModel] | None = None
    Type: StrictStr | None = None
    ValidFrom: datetime.datetime | StrictStr | None = None
    ValidUntil: datetime.datetime | StrictStr | None = None
    InstanceInterruptionBehavior: StrictStr | None = None
