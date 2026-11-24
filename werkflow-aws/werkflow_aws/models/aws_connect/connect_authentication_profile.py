from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ConnectAuthenticationProfile(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    AllowedIps: list[StrictStr] | None = None
    BlockedIps: list[StrictStr] | None = None
    IsDefault: StrictBool | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    PeriodicSessionDuration: StrictInt | None = None
    MaxSessionDuration: StrictInt | None = None
    SessionInactivityDuration: StrictInt | None = None
    SessionInactivityHandlingEnabled: StrictBool | None = None
