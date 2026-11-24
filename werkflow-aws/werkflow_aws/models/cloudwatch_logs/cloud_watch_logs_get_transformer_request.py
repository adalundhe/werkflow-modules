from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsGetTransformerRequest(BaseModel):
    logGroupIdentifier: StrictStr
