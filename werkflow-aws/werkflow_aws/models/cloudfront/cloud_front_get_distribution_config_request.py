from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetDistributionConfigRequest(BaseModel):
    Id: StrictStr
