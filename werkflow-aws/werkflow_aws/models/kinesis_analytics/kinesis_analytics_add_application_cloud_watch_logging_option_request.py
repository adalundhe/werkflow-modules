from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_cloud_watch_logging_option import KinesisAnalyticsCloudWatchLoggingOption


class KinesisAnalyticsAddApplicationCloudWatchLoggingOptionRequest(BaseModel):
    ApplicationName: StrictStr
    CloudWatchLoggingOption: KinesisAnalyticsCloudWatchLoggingOption
    CurrentApplicationVersionId: StrictInt | None = None
    ConditionalToken: StrictStr | None = None
