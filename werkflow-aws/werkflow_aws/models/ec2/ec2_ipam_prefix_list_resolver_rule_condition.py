from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_ipam_resource_tag import EC2IpamResourceTag


class EC2IpamPrefixListResolverRuleCondition(BaseModel):
    Operation: StrictStr | None = None
    IpamPoolId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceOwner: StrictStr | None = None
    ResourceRegion: StrictStr | None = None
    ResourceTag: EC2IpamResourceTag | None = None
    Cidr: StrictStr | None = None
