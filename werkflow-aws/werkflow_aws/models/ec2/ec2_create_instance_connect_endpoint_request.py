from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateInstanceConnectEndpointRequest(BaseModel):
    SubnetId: StrictStr
    DryRun: StrictBool | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    PreserveClientIp: StrictBool | None = None
    ClientToken: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    IpAddressType: Literal['ipv4', 'dualstack', 'ipv6'] | None = None
