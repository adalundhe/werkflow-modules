from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetDistributionRequest(BaseModel):
    Id: StrictStr
