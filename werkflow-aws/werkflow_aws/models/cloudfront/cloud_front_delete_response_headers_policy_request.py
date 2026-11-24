from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDeleteResponseHeadersPolicyRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr | None = None
