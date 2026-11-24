from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailResetDistributionCacheRequest(BaseModel):
    distributionName: StrictStr | None = None
