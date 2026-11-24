from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsPutDestinationPolicyRequest(BaseModel):
    destinationName: StrictStr
    accessPolicy: StrictStr
    forceUpdate: StrictBool | None = None
