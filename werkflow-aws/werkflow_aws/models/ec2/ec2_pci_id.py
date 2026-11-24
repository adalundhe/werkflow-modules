from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PciId(BaseModel):
    DeviceId: StrictStr | None = None
    VendorId: StrictStr | None = None
    SubsystemId: StrictStr | None = None
    SubsystemVendorId: StrictStr | None = None
