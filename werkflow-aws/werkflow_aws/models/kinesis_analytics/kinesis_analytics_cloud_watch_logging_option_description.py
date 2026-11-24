from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsCloudWatchLoggingOptionDescription(BaseModel):
    CloudWatchLoggingOptionId: StrictStr | None = None
    LogStreamARN: StrictStr | None = None
    RoleARN: StrictStr | None = None
