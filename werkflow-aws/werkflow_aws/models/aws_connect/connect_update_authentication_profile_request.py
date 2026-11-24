from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ConnectUpdateAuthenticationProfileRequest(BaseModel):
    AuthenticationProfileId: StrictStr
    InstanceId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    AllowedIps: list[StrictStr] | None = None
    BlockedIps: list[StrictStr] | None = None
    PeriodicSessionDuration: StrictInt | None = None
    SessionInactivityDuration: StrictInt | None = None
    SessionInactivityHandlingEnabled: StrictBool | None = None
