from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDirectoryConnectSettings(BaseModel):
    VpcId: StrictStr
    SubnetIds: list[StrictStr]
    CustomerUserName: StrictStr
    CustomerDnsIps: list[StrictStr] | None = None
    CustomerDnsIpsV6: list[StrictStr] | None = None
