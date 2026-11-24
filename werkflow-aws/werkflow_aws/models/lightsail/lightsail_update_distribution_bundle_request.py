from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailUpdateDistributionBundleRequest(BaseModel):
    distributionName: StrictStr | None = None
    bundleId: StrictStr | None = None
