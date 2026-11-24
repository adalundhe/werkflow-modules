from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_group_identifier import EC2GroupIdentifier
from .ec2_instance_state import EC2InstanceState
from .ec2_placement import EC2Placement
from .ec2_tag import EC2Tag


class EC2Instance(BaseModel):
    InstanceId: StrictStr | None = None
    ImageId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    KeyName: StrictStr | None = None
    LaunchTime: datetime.datetime | None = None
    State: EC2InstanceState | None = None
    Placement: EC2Placement | None = None
    PrivateDnsName: StrictStr | None = None
    PublicDnsName: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
    PublicIpAddress: StrictStr | None = None
    SubnetId: StrictStr | None = None
    VpcId: StrictStr | None = None
    Architecture: StrictStr | None = None
    SecurityGroups: list[EC2GroupIdentifier] | None = None
    Tags: list[EC2Tag] | None = None
