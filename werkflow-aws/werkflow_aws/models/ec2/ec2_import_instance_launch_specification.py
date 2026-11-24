from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_placement_model import EC2PlacementModel
from .ec2_user_data import EC2UserData


class EC2ImportInstanceLaunchSpecification(BaseModel):
    Architecture: Literal['i386', 'x86_64', 'arm64', 'x86_64_mac', 'arm64_mac'] | None = None
    GroupNames: list[StrictStr] | None = None
    GroupIds: list[StrictStr] | None = None
    AdditionalInfo: StrictStr | None = None
    UserData: EC2UserData | None = None
    InstanceType: StrictStr | None = None
    Placement: EC2PlacementModel | None = None
    Monitoring: StrictBool | None = None
    SubnetId: StrictStr | None = None
    InstanceInitiatedShutdownBehavior: Literal['stop', 'terminate'] | None = None
    PrivateIpAddress: StrictStr | None = None
