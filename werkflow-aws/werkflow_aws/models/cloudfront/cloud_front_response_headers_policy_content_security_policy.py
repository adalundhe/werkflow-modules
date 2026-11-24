from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFrontResponseHeadersPolicyContentSecurityPolicy(BaseModel):
    Override: StrictBool | None = None
    ContentSecurityPolicy: StrictStr | None = None
