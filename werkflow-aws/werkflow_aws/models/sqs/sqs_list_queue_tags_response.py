from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSListQueueTagsResponse(BaseModel):
    Tags: dict[StrictStr, StrictStr] | None = None
