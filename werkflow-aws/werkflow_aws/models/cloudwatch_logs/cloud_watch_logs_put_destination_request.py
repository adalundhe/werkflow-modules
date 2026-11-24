from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsPutDestinationRequest(BaseModel):
    destinationName: StrictStr
    targetArn: StrictStr
    roleArn: StrictStr
    tags: dict[StrictStr, StrictStr] | None = None
