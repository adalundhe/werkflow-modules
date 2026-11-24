from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontIpamCidrConfig(BaseModel):
    Cidr: StrictStr | None = None
    IpamPoolArn: StrictStr | None = None
    AnycastIp: StrictStr | None = None
    Status: StrictStr | None = None
