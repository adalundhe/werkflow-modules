from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2AllocateAddressRequest(BaseModel):
    Domain: Literal['vpc', 'standard'] | None = None
    Address: StrictStr | None = None
    PublicIpv4Pool: StrictStr | None = None
    NetworkBorderGroup: StrictStr | None = None
    CustomerOwnedIpv4Pool: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    IpamPoolId: StrictStr | None = None
    DryRun: StrictBool | None = None
