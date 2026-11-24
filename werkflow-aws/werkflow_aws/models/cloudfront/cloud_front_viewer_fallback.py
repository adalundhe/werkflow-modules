from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontViewerFallback(BaseModel):
    DistributionId: StrictStr | None = None
