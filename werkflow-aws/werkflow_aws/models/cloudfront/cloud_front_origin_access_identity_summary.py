from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontOriginAccessIdentitySummary(BaseModel):
    Id: StrictStr | None = None
    S3CanonicalUserId: StrictStr | None = None
    Comment: StrictStr | None = None
