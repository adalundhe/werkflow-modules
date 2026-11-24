from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_add_ipam_operating_region import EC2AddIpamOperatingRegion
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateIpamResourceDiscoveryRequest(BaseModel):
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
    OperatingRegions: list[EC2AddIpamOperatingRegion] | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ClientToken: StrictStr | None = None
