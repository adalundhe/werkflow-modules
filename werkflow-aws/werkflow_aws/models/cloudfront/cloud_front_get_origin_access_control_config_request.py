from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetOriginAccessControlConfigRequest(BaseModel):
    Id: StrictStr
