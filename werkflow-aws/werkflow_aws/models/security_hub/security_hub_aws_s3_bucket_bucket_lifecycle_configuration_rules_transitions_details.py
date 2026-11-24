from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails(BaseModel):
    Date: StrictStr | None = None
    Days: StrictInt | None = None
    StorageClass: StrictStr | None = None
