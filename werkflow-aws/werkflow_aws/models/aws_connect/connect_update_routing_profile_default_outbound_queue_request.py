from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateRoutingProfileDefaultOutboundQueueRequest(BaseModel):
    InstanceId: StrictStr
    RoutingProfileId: StrictStr
    DefaultOutboundQueueId: StrictStr
