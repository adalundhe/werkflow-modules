from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsS3BucketWebsiteConfigurationRoutingRuleCondition(BaseModel):
    HttpErrorCodeReturnedEquals: StrictStr | None = None
    KeyPrefixEquals: StrictStr | None = None
