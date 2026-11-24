from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetCloudFrontOriginAccessIdentityConfigRequest(BaseModel):
    Id: StrictStr
