from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .timestream_query_account_settings_notification_configuration import TimestreamQueryAccountSettingsNotificationConfiguration
from .timestream_query_last_update import TimestreamQueryLastUpdate


class TimestreamQueryProvisionedCapacityResponse(BaseModel):
    ActiveQueryTCU: StrictInt | None = None
    NotificationConfiguration: TimestreamQueryAccountSettingsNotificationConfiguration | None = None
    LastUpdate: TimestreamQueryLastUpdate | None = None
