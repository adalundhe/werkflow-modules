from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsS3BucketWebsiteConfigurationRoutingRuleRedirect(BaseModel):
    Hostname: StrictStr | None = None
    HttpRedirectCode: StrictStr | None = None
    Protocol: StrictStr | None = None
    ReplaceKeyPrefixWith: StrictStr | None = None
    ReplaceKeyWith: StrictStr | None = None
