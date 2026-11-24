from __future__ import annotations
from pydantic import BaseModel
from .security_lake_https_notification_configuration import SecurityLakeHttpsNotificationConfiguration
from .security_lake_sqs_notification_configuration import SecurityLakeSqsNotificationConfiguration


class SecurityLakeNotificationConfiguration(BaseModel):
    httpsNotificationConfiguration: SecurityLakeHttpsNotificationConfiguration | None = None
    sqsNotificationConfiguration: SecurityLakeSqsNotificationConfiguration | None = None
