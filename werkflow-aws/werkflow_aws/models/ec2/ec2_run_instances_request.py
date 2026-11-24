from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from typing import Any
from .ec2_placement import EC2Placement
from .ec2_tag_specification import EC2TagSpecification


class EC2RunInstancesRequest(BaseModel):
    ImageId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    MinCount: StrictInt = 1
    MaxCount: StrictInt = 1
    KeyName: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    SecurityGroups: list[StrictStr] | None = None
    SubnetId: StrictStr | None = None
    UserData: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecification] | None = None
    Placement: EC2Placement | None = None
    BlockDeviceMappings: list[dict[str, Any]] | None = None
    IamInstanceProfile: dict[str, StrictStr] | None = None
    EbsOptimized: StrictBool | None = None
    DryRun: StrictBool | None = None
