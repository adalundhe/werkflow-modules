from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListQueueQuickConnectsRequest(BaseModel):
    InstanceId: StrictStr
    QueueId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
