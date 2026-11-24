from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontOriginAccessIdentityConfig(BaseModel):
    CallerReference: StrictStr | None = None
    Comment: StrictStr | None = None
