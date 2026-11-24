from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DirectoryServiceRadiusSettings(BaseModel):
    RadiusServers: list[StrictStr] | None = None
    RadiusServersIpv6: list[StrictStr] | None = None
    RadiusPort: StrictInt | None = None
    RadiusTimeout: StrictInt | None = None
    RadiusRetries: StrictInt | None = None
    SharedSecret: StrictStr | None = None
    AuthenticationProtocol: StrictStr | None = None
    DisplayLabel: StrictStr | None = None
    UseSameUsername: StrictBool | None = None
