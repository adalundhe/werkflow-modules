from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamNetworkAccessConfiguration(BaseModel):
    EniPrivateIpAddress: StrictStr | None = None
    EniIpv6Addresses: list[StrictStr] | None = None
    EniId: StrictStr | None = None
