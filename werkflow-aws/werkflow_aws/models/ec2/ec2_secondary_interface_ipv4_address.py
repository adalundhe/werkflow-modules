from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SecondaryInterfaceIpv4Address(BaseModel):
    PrivateIpAddress: StrictStr | None = None
