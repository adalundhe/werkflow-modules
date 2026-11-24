from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteTransformerRequest(BaseModel):
    logGroupIdentifier: StrictStr
