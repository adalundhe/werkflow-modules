from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_add_ipam_operating_region import EC2AddIpamOperatingRegion
from .ec2_remove_ipam_operating_region import EC2RemoveIpamOperatingRegion


class EC2ModifyIpamRequest(BaseModel):
    IpamId: StrictStr
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
    AddOperatingRegions: list[EC2AddIpamOperatingRegion] | None = None
    RemoveOperatingRegions: list[EC2RemoveIpamOperatingRegion] | None = None
    Tier: Literal['free', 'advanced'] | None = None
    EnablePrivateGua: StrictBool | None = None
    MeteredAccount: Literal['ipam-owner', 'resource-owner'] | None = None
