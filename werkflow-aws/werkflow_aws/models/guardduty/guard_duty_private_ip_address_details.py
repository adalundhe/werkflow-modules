from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyPrivateIpAddressDetails(BaseModel):
    PrivateDnsName: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
