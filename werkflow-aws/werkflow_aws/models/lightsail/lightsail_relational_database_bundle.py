from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class LightsailRelationalDatabaseBundle(BaseModel):
    bundleId: StrictStr | None = None
    name: StrictStr | None = None
    price: StrictFloat | StrictInt | None = None
    ramSizeInGb: StrictFloat | StrictInt | None = None
    diskSizeInGb: StrictInt | None = None
    transferPerMonthInGb: StrictInt | None = None
    cpuCount: StrictInt | None = None
    isEncrypted: StrictBool | None = None
    isActive: StrictBool | None = None
