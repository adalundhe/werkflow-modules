from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetAnycastIpListRequest(BaseModel):
    Id: StrictStr
