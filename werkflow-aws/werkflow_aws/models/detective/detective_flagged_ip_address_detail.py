from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveFlaggedIpAddressDetail(BaseModel):
    IpAddress: StrictStr | None = None
    Reason: StrictStr | None = None
