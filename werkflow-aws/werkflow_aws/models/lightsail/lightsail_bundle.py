from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class LightsailBundle(BaseModel):
    price: StrictFloat | StrictInt | None = None
    cpuCount: StrictInt | None = None
    diskSizeInGb: StrictInt | None = None
    bundleId: StrictStr | None = None
    instanceType: StrictStr | None = None
    isActive: StrictBool | None = None
    name: StrictStr | None = None
    power: StrictInt | None = None
    ramSizeInGb: StrictFloat | StrictInt | None = None
    transferPerMonthInGb: StrictInt | None = None
    supportedPlatforms: list[StrictStr] | None = None
    supportedAppCategories: list[StrictStr] | None = None
    publicIpv4AddressCount: StrictInt | None = None
