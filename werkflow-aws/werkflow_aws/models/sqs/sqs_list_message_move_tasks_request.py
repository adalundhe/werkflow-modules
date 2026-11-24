from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SQSListMessageMoveTasksRequest(BaseModel):
    SourceArn: StrictStr
    MaxResults: StrictInt | None = None
