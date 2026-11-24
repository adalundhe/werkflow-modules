from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_request_spot_launch_specification import EC2RequestSpotLaunchSpecification
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2RequestSpotInstancesRequest(BaseModel):
    LaunchSpecification: EC2RequestSpotLaunchSpecification | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    InstanceInterruptionBehavior: Literal['hibernate', 'stop', 'terminate'] | None = None
    DryRun: StrictBool | None = None
    SpotPrice: StrictStr | None = None
    ClientToken: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    Type: Literal['one-time', 'persistent'] | None = None
    ValidFrom: datetime.datetime | StrictStr | None = None
    ValidUntil: datetime.datetime | StrictStr | None = None
    LaunchGroup: StrictStr | None = None
    AvailabilityZoneGroup: StrictStr | None = None
    BlockDurationMinutes: StrictInt | None = None
