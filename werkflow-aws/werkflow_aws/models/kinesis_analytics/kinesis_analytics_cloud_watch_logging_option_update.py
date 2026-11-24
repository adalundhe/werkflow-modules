from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsCloudWatchLoggingOptionUpdate(BaseModel):
    CloudWatchLoggingOptionId: StrictStr
    LogStreamARNUpdate: StrictStr | None = None
