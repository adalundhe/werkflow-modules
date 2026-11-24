from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetStreamingDistributionRequest(BaseModel):
    Id: StrictStr
