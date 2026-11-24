from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateSubnetRequest(BaseModel):
    VpcId: StrictStr
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    CidrBlock: StrictStr | None = None
    Ipv6CidrBlock: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    Ipv6Native: StrictBool | None = None
    Ipv4IpamPoolId: StrictStr | None = None
    Ipv4NetmaskLength: StrictInt | None = None
    Ipv6IpamPoolId: StrictStr | None = None
    Ipv6NetmaskLength: StrictInt | None = None
    DryRun: StrictBool | None = None
