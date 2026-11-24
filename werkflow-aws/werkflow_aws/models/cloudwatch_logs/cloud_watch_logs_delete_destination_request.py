from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteDestinationRequest(BaseModel):
    destinationName: StrictStr
