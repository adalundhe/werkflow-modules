from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .awss3_notification_configuration import AWSS3NotificationConfiguration


class AWSS3PutBucketNotificationConfigurationRequest(BaseModel):
    Bucket: StrictStr
    NotificationConfiguration: AWSS3NotificationConfiguration
    ExpectedBucketOwner: StrictStr | None = None
    SkipDestinationValidation: StrictBool | None = None
