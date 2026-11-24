from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetails(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
