from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class CloudFrontResponseHeadersPolicyStrictTransportSecurity(BaseModel):
    Override: StrictBool | None = None
    IncludeSubdomains: StrictBool | None = None
    Preload: StrictBool | None = None
    AccessControlMaxAgeSec: StrictInt | None = None
