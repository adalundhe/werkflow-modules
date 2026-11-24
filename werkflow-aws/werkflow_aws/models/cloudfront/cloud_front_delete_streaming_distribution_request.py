from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDeleteStreamingDistributionRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr | None = None
