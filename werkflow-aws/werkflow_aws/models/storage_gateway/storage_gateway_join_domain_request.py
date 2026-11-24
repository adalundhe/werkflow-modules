from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayJoinDomainRequest(BaseModel):
    GatewayARN: StrictStr
    DomainName: StrictStr
    UserName: StrictStr
    Password: StrictStr
    OrganizationalUnit: StrictStr | None = None
    DomainControllers: list[StrictStr] | None = None
    TimeoutInSeconds: StrictInt | None = None
