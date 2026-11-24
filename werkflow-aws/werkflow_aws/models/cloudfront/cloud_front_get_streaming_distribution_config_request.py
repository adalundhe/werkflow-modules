from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetStreamingDistributionConfigRequest(BaseModel):
    Id: StrictStr
