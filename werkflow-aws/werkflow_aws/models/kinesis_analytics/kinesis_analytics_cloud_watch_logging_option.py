from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsCloudWatchLoggingOption(BaseModel):
    LogStreamARN: StrictStr
