from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftNetworkInterface(BaseModel):
    NetworkInterfaceId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    Ipv6Address: StrictStr | None = None
