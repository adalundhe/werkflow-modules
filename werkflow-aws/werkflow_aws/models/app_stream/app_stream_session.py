from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_stream_network_access_configuration import AppStreamNetworkAccessConfiguration


class AppStreamSession(BaseModel):
    Id: StrictStr | None = None
    UserId: StrictStr | None = None
    StackName: StrictStr | None = None
    FleetName: StrictStr | None = None
    State: StrictStr | None = None
    ConnectionState: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    MaxExpirationTime: datetime.datetime | StrictStr | None = None
    AuthenticationType: StrictStr | None = None
    NetworkAccessConfiguration: AppStreamNetworkAccessConfiguration | None = None
    InstanceId: StrictStr | None = None
    InstanceDrainStatus: StrictStr | None = None
