from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2VpnConnectionDeviceType(BaseModel):
    VpnConnectionDeviceTypeId: StrictStr | None = None
    Vendor: StrictStr | None = None
    Platform: StrictStr | None = None
    Software: StrictStr | None = None
