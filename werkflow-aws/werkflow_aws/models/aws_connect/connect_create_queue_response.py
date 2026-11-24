from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateQueueResponse(BaseModel):
    QueueArn: StrictStr | None = None
    QueueId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
