from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleImportJobVPCConnectionOverrideParameters(BaseModel):
    VPCConnectionId: StrictStr | None = None
    Name: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    DnsResolvers: list[StrictStr] | None = None
    RoleArn: StrictStr | None = None
