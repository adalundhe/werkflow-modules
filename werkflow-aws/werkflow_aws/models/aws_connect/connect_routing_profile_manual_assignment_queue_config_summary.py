from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectRoutingProfileManualAssignmentQueueConfigSummary(BaseModel):
    QueueId: StrictStr | None = None
    QueueArn: StrictStr | None = None
    QueueName: StrictStr | None = None
    Channel: StrictStr | None = None
