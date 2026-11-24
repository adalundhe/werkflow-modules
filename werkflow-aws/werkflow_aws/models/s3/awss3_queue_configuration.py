from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_notification_configuration_filter import AWSS3NotificationConfigurationFilter


class AWSS3QueueConfiguration(BaseModel):
    Id: StrictStr | None = None
    QueueArn: StrictStr | None = None
    Events: list[StrictStr] | None = None
    Filter: AWSS3NotificationConfigurationFilter | None = None
