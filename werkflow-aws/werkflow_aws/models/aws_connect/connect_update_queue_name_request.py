from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateQueueNameRequest(BaseModel):
    InstanceId: StrictStr
    QueueId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
