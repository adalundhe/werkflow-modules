from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class LightsailContainerServicePower(BaseModel):
    powerId: StrictStr | None = None
    price: StrictFloat | StrictInt | None = None
    cpuCount: StrictFloat | StrictInt | None = None
    ramSizeInGb: StrictFloat | StrictInt | None = None
    name: StrictStr | None = None
    isActive: StrictBool | None = None
