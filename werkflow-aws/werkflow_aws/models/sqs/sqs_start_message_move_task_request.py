from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SQSStartMessageMoveTaskRequest(BaseModel):
    SourceArn: StrictStr
    DestinationArn: StrictStr | None = None
    MaxNumberOfMessagesPerSecond: StrictInt | None = None
