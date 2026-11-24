from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SQSListDeadLetterSourceQueuesRequest(BaseModel):
    QueueUrl: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
