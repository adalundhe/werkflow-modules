from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontS3Origin(BaseModel):
    DomainName: StrictStr | None = None
    OriginAccessIdentity: StrictStr | None = None
