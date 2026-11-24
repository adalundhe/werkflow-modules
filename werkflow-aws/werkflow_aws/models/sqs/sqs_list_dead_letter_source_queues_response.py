from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSListDeadLetterSourceQueuesResponse(BaseModel):
    queueUrls: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
