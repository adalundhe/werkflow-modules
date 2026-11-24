from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails(BaseModel):
    DaysAfterInitiation: StrictInt | None = None
