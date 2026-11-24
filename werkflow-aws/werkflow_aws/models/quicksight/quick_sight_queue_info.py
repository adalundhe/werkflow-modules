from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightQueueInfo(BaseModel):
    WaitingOnIngestion: StrictStr | None = None
    QueuedIngestion: StrictStr | None = None
