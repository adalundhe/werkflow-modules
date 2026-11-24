from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SecondaryInterfacePrivateIpAddressSpecification(BaseModel):
    PrivateIpAddress: StrictStr | None = None
