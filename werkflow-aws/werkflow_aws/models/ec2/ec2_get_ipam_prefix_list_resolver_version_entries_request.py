from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2GetIpamPrefixListResolverVersionEntriesRequest(BaseModel):
    IpamPrefixListResolverId: StrictStr
    IpamPrefixListResolverVersion: StrictInt
    DryRun: StrictBool | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
