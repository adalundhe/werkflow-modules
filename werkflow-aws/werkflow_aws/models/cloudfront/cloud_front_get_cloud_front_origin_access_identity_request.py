from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetCloudFrontOriginAccessIdentityRequest(BaseModel):
    Id: StrictStr
