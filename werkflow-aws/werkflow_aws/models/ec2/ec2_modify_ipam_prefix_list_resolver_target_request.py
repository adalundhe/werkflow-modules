from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ModifyIpamPrefixListResolverTargetRequest(BaseModel):
    IpamPrefixListResolverTargetId: StrictStr
    DryRun: StrictBool | None = None
    DesiredVersion: StrictInt | None = None
    TrackLatestVersion: StrictBool | None = None
    ClientToken: StrictStr | None = None
