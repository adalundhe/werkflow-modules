from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDeleteDistributionRequest(BaseModel):
    distributionName: StrictStr | None = None
