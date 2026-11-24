from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel
from .ec2_request_ipam_resource_tag import EC2RequestIpamResourceTag


class EC2GetIpamResourceCidrsRequest(BaseModel):
    IpamScopeId: StrictStr
    DryRun: StrictBool | None = None
    Filters: list[EC2FilterModel] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    IpamPoolId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: Literal['vpc', 'subnet', 'eip', 'public-ipv4-pool', 'ipv6-pool', 'eni', 'anycast-ip-list'] | None = None
    ResourceTag: EC2RequestIpamResourceTag | None = None
    ResourceOwner: StrictStr | None = None
