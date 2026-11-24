from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightNetworkInterface(BaseModel):
    SubnetId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    Status: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
