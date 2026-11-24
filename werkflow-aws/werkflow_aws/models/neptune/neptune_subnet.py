from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_availability_zone import NeptuneAvailabilityZone


class NeptuneSubnet(BaseModel):
    SubnetIdentifier: StrictStr | None = None
    SubnetAvailabilityZone: NeptuneAvailabilityZone | None = None
    SubnetStatus: StrictStr | None = None
