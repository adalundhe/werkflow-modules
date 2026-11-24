from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class LightsailDistributionBundle(BaseModel):
    bundleId: StrictStr | None = None
    name: StrictStr | None = None
    price: StrictFloat | StrictInt | None = None
    transferPerMonthInGb: StrictInt | None = None
    isActive: StrictBool | None = None
