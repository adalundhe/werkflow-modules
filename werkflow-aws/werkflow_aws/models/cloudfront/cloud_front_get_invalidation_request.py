from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetInvalidationRequest(BaseModel):
    DistributionId: StrictStr
    Id: StrictStr
