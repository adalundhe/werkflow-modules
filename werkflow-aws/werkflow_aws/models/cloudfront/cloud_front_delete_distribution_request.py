from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDeleteDistributionRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr | None = None
