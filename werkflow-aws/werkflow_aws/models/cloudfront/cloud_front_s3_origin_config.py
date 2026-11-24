from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontS3OriginConfig(BaseModel):
    OriginAccessIdentity: StrictStr | None = None
    OriginReadTimeout: StrictInt | None = None
