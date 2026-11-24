from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Ipv6Range(BaseModel):
    Description: StrictStr | None = None
    CidrIpv6: StrictStr | None = None
