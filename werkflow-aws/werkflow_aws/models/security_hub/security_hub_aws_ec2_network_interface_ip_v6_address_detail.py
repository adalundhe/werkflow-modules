from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2NetworkInterfaceIpV6AddressDetail(BaseModel):
    IpV6Address: StrictStr | None = None
