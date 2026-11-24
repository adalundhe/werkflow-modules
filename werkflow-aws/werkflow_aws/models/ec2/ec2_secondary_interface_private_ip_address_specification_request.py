from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SecondaryInterfacePrivateIpAddressSpecificationRequest(BaseModel):
    PrivateIpAddress: StrictStr | None = None
