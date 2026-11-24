from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_ipam_operating_region import EC2IpamOperatingRegion
from .ec2_ipam_organizational_unit_exclusion import EC2IpamOrganizationalUnitExclusion
from .ec2_tag_model import EC2TagModel


class EC2IpamResourceDiscovery(BaseModel):
    OwnerId: StrictStr | None = None
    IpamResourceDiscoveryId: StrictStr | None = None
    IpamResourceDiscoveryArn: StrictStr | None = None
    IpamResourceDiscoveryRegion: StrictStr | None = None
    Description: StrictStr | None = None
    OperatingRegions: list[EC2IpamOperatingRegion] | None = None
    IsDefault: StrictBool | None = None
    State: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    OrganizationalUnitExclusions: list[EC2IpamOrganizationalUnitExclusion] | None = None
