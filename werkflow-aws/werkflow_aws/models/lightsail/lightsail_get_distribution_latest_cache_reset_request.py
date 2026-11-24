from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetDistributionLatestCacheResetRequest(BaseModel):
    distributionName: StrictStr | None = None
