from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDisassociateQueueQuickConnectsRequest(BaseModel):
    InstanceId: StrictStr
    QueueId: StrictStr
    QuickConnectIds: list[StrictStr]
