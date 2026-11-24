from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDirectoryConnectSettingsDescription(BaseModel):
    VpcId: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    CustomerUserName: StrictStr | None = None
    SecurityGroupId: StrictStr | None = None
    AvailabilityZones: list[StrictStr] | None = None
    ConnectIps: list[StrictStr] | None = None
    ConnectIpsV6: list[StrictStr] | None = None
