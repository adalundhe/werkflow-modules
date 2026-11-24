from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SQSListMessageMoveTasksResultEntry(BaseModel):
    TaskHandle: StrictStr | None = None
    Status: StrictStr | None = None
    SourceArn: StrictStr | None = None
    DestinationArn: StrictStr | None = None
    MaxNumberOfMessagesPerSecond: StrictInt | None = None
    ApproximateNumberOfMessagesMoved: StrictInt | None = None
    ApproximateNumberOfMessagesToMove: StrictInt | None = None
    FailureReason: StrictStr | None = None
    StartedTimestamp: StrictInt | None = None
