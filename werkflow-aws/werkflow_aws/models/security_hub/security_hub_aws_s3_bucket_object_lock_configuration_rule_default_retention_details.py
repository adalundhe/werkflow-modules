from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails(BaseModel):
    Days: StrictInt | None = None
    Mode: StrictStr | None = None
    Years: StrictInt | None = None
