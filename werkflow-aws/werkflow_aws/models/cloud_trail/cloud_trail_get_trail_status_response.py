from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class CloudTrailGetTrailStatusResponse(BaseModel):
    IsLogging: StrictBool | None = None
    LatestDeliveryError: StrictStr | None = None
    LatestNotificationError: StrictStr | None = None
    LatestDeliveryTime: datetime.datetime | StrictStr | None = None
    LatestNotificationTime: datetime.datetime | StrictStr | None = None
    StartLoggingTime: datetime.datetime | StrictStr | None = None
    StopLoggingTime: datetime.datetime | StrictStr | None = None
    LatestCloudWatchLogsDeliveryError: StrictStr | None = None
    LatestCloudWatchLogsDeliveryTime: datetime.datetime | StrictStr | None = None
    LatestDigestDeliveryTime: datetime.datetime | StrictStr | None = None
    LatestDigestDeliveryError: StrictStr | None = None
    LatestDeliveryAttemptTime: StrictStr | None = None
    LatestNotificationAttemptTime: StrictStr | None = None
    LatestNotificationAttemptSucceeded: StrictStr | None = None
    LatestDeliveryAttemptSucceeded: StrictStr | None = None
    TimeLoggingStarted: StrictStr | None = None
    TimeLoggingStopped: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
