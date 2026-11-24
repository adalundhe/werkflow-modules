from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_cloud_watch_logging_option_description import KinesisAnalyticsCloudWatchLoggingOptionDescription


class KinesisAnalyticsAddApplicationCloudWatchLoggingOptionResponse(BaseModel):
    ApplicationARN: StrictStr | None = None
    ApplicationVersionId: StrictInt | None = None
    CloudWatchLoggingOptionDescriptions: list[KinesisAnalyticsCloudWatchLoggingOptionDescription] | None = None
    OperationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
