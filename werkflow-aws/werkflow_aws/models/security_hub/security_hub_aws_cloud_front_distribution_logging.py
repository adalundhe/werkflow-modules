from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsCloudFrontDistributionLogging(BaseModel):
    Bucket: StrictStr | None = None
    Enabled: StrictBool | None = None
    IncludeCookies: StrictBool | None = None
    Prefix: StrictStr | None = None
