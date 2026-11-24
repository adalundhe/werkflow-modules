from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsCloudFrontDistributionDefaultCacheBehavior(BaseModel):
    ViewerProtocolPolicy: StrictStr | None = None
