from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails(BaseModel):
    Days: StrictInt | None = None
    StorageClass: StrictStr | None = None
