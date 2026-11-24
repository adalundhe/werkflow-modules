from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_s3_bucket_notification_configuration_filter import SecurityHubAwsS3BucketNotificationConfigurationFilter


class SecurityHubAwsS3BucketNotificationConfigurationDetail(BaseModel):
    Events: list[StrictStr] | None = None
    Filter: SecurityHubAwsS3BucketNotificationConfigurationFilter | None = None
    Destination: StrictStr | None = None
    Type: StrictStr | None = None
