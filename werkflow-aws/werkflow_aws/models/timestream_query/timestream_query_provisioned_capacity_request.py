from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .timestream_query_account_settings_notification_configuration import TimestreamQueryAccountSettingsNotificationConfiguration


class TimestreamQueryProvisionedCapacityRequest(BaseModel):
    TargetQueryTCU: StrictInt
    NotificationConfiguration: TimestreamQueryAccountSettingsNotificationConfiguration | None = None
