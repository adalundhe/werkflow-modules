from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetResponseHeadersPolicyRequest(BaseModel):
    Id: StrictStr
