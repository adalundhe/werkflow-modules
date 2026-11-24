from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectQueueQuickConnectConfig(BaseModel):
    QueueId: StrictStr | None = None
    ContactFlowId: StrictStr | None = None
