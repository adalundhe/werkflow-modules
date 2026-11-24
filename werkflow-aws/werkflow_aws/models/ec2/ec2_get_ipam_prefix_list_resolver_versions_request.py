from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2GetIpamPrefixListResolverVersionsRequest(BaseModel):
    IpamPrefixListResolverId: StrictStr
    DryRun: StrictBool | None = None
    IpamPrefixListResolverVersions: list[StrictInt] | None = None
    MaxResults: StrictInt | None = None
    Filters: list[EC2FilterModel] | None = None
    NextToken: StrictStr | None = None
