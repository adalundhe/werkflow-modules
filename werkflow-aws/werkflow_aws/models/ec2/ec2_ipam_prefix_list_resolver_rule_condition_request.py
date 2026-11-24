from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ec2_request_ipam_resource_tag import EC2RequestIpamResourceTag


class EC2IpamPrefixListResolverRuleConditionRequest(BaseModel):
    Operation: Literal['equals', 'not-equals', 'subnet-of']
    IpamPoolId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceOwner: StrictStr | None = None
    ResourceRegion: StrictStr | None = None
    ResourceTag: EC2RequestIpamResourceTag | None = None
    Cidr: StrictStr | None = None
