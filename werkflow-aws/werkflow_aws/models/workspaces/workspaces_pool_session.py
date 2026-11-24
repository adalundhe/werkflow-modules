from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .work_spaces_network_access_configuration import WorkSpacesNetworkAccessConfiguration


class WorkspacesPoolSession(BaseModel):
    AuthenticationType: StrictStr | None = None
    ConnectionState: StrictStr | None = None
    SessionId: StrictStr | None = None
    InstanceId: StrictStr | None = None
    PoolId: StrictStr | None = None
    ExpirationTime: datetime.datetime | StrictStr | None = None
    NetworkAccessConfiguration: WorkSpacesNetworkAccessConfiguration | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    UserId: StrictStr | None = None
