from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontVpcOriginConfig(BaseModel):
    VpcOriginId: StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
    OriginReadTimeout: StrictInt | None = None
    OriginKeepaliveTimeout: StrictInt | None = None
    OriginHttpVersion: StrictStr | None = None
