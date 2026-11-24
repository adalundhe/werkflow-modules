from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDnsConfiguration(BaseModel):
    Domain: StrictStr | None = None
    Status: StrictStr | None = None
    Reason: StrictStr | None = None
