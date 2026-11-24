from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectRoutingProfileQueueConfigSummary(BaseModel):
    QueueId: StrictStr | None = None
    QueueArn: StrictStr | None = None
    QueueName: StrictStr | None = None
    Priority: StrictInt | None = None
    Delay: StrictInt | None = None
    Channel: StrictStr | None = None
