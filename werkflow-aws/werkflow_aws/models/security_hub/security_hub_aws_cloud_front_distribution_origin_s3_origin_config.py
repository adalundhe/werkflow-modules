from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsCloudFrontDistributionOriginS3OriginConfig(BaseModel):
    OriginAccessIdentity: StrictStr | None = None
