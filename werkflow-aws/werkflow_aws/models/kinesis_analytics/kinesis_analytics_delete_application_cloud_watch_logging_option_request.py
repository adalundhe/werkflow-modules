from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsDeleteApplicationCloudWatchLoggingOptionRequest(BaseModel):
    ApplicationName: StrictStr
    CloudWatchLoggingOptionId: StrictStr
    CurrentApplicationVersionId: StrictInt | None = None
    ConditionalToken: StrictStr | None = None
