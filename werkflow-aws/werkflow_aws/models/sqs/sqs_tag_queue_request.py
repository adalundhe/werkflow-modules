from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSTagQueueRequest(BaseModel):
    QueueUrl: StrictStr
    Tags: dict[StrictStr, StrictStr]
