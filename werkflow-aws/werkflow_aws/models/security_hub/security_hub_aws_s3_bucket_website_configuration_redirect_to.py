from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsS3BucketWebsiteConfigurationRedirectTo(BaseModel):
    Hostname: StrictStr | None = None
    Protocol: StrictStr | None = None
