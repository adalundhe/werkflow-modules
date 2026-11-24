from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudHSMHsm(BaseModel):
    AvailabilityZone: StrictStr | None = None
    ClusterId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    EniId: StrictStr | None = None
    EniIp: StrictStr | None = None
    EniIpV6: StrictStr | None = None
    HsmId: StrictStr | None = None
    HsmType: StrictStr | None = None
    State: StrictStr | None = None
    StateMessage: StrictStr | None = None
