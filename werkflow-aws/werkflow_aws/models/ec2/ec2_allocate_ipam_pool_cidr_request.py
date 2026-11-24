from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2AllocateIpamPoolCidrRequest(BaseModel):
    IpamPoolId: StrictStr
    DryRun: StrictBool | None = None
    Cidr: StrictStr | None = None
    NetmaskLength: StrictInt | None = None
    ClientToken: StrictStr | None = None
    Description: StrictStr | None = None
    PreviewNextCidr: StrictBool | None = None
    AllowedCidrs: list[StrictStr] | None = None
    DisallowedCidrs: list[StrictStr] | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
