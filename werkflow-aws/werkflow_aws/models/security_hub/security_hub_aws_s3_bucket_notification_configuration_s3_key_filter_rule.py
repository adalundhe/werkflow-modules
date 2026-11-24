from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsS3BucketNotificationConfigurationS3KeyFilterRule(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
