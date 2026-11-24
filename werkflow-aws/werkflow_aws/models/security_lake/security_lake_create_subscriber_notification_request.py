from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_lake_notification_configuration import SecurityLakeNotificationConfiguration


class SecurityLakeCreateSubscriberNotificationRequest(BaseModel):
    configuration: SecurityLakeNotificationConfiguration
    subscriberId: StrictStr
