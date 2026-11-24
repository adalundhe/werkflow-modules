from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class BatchUpdateJobQueueResponse(BaseModel):
    jobQueueName: StrictStr | None = None
    jobQueueArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
