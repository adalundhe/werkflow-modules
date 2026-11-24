from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectUpdateQueueMaxContactsRequest(BaseModel):
    InstanceId: StrictStr
    QueueId: StrictStr
    MaxContacts: StrictInt | None = None
