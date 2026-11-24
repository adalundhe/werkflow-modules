from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .ec2_ipam_resource_tag import EC2IpamResourceTag


class EC2IpamResourceCidr(BaseModel):
    IpamId: StrictStr | None = None
    IpamScopeId: StrictStr | None = None
    IpamPoolId: StrictStr | None = None
    ResourceRegion: StrictStr | None = None
    ResourceOwnerId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceName: StrictStr | None = None
    ResourceCidr: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceTags: list[EC2IpamResourceTag] | None = None
    IpUsage: StrictFloat | StrictInt | None = None
    ComplianceStatus: StrictStr | None = None
    ManagementState: StrictStr | None = None
    OverlapStatus: StrictStr | None = None
    VpcId: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
