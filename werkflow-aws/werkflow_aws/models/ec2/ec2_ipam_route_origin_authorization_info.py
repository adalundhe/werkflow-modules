from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2IpamRouteOriginAuthorizationInfo(BaseModel):
    Cidr: StrictStr | None = None
    Asn: StrictStr | None = None
    MaxLength: StrictInt | None = None
