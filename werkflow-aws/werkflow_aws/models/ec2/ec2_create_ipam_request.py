from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_add_ipam_operating_region import EC2AddIpamOperatingRegion
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateIpamRequest(BaseModel):
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
    OperatingRegions: list[EC2AddIpamOperatingRegion] | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ClientToken: StrictStr | None = None
    Tier: Literal['free', 'advanced'] | None = None
    EnablePrivateGua: StrictBool | None = None
    MeteredAccount: Literal['ipam-owner', 'resource-owner'] | None = None
