from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateRoutingProfileNameRequest(BaseModel):
    InstanceId: StrictStr
    RoutingProfileId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
