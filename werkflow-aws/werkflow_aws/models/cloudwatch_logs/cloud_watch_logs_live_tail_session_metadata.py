from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CloudWatchLogsLiveTailSessionMetadata(BaseModel):
    sampled: StrictBool | None = None
