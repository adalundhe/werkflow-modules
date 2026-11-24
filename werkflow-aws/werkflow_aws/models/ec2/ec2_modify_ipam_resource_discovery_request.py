from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_add_ipam_operating_region import EC2AddIpamOperatingRegion
from .ec2_add_ipam_organizational_unit_exclusion import EC2AddIpamOrganizationalUnitExclusion
from .ec2_remove_ipam_operating_region import EC2RemoveIpamOperatingRegion
from .ec2_remove_ipam_organizational_unit_exclusion import EC2RemoveIpamOrganizationalUnitExclusion


class EC2ModifyIpamResourceDiscoveryRequest(BaseModel):
    IpamResourceDiscoveryId: StrictStr
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
    AddOperatingRegions: list[EC2AddIpamOperatingRegion] | None = None
    RemoveOperatingRegions: list[EC2RemoveIpamOperatingRegion] | None = None
    AddOrganizationalUnitExclusions: list[EC2AddIpamOrganizationalUnitExclusion] | None = None
    RemoveOrganizationalUnitExclusions: list[EC2RemoveIpamOrganizationalUnitExclusion] | None = None
