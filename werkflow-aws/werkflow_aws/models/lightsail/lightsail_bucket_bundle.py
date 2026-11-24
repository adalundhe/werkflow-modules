from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class LightsailBucketBundle(BaseModel):
    bundleId: StrictStr | None = None
    name: StrictStr | None = None
    price: StrictFloat | StrictInt | None = None
    storagePerMonthInGb: StrictInt | None = None
    transferPerMonthInGb: StrictInt | None = None
    isActive: StrictBool | None = None
