from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSListQueuesResponse(BaseModel):
    QueueUrls: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
